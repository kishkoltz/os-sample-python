from flask import request, flash, render_template
from app import app, db
from app.models import Author, Book
from app.forms import ImportBooks, AddBook
import requests, json

@app.route('/')
@app.route('/books')
def books():
    books = Book.query.all()
    data = []
    for b in books:
        author = Author.query.get(b.author_id)
        data.append({
        "author":author.name,
        "title":b.title,
        "genre":b.genre,
        "description":b.description
        })
    return render_template('books.html', title='Books', data=data)
@app.route('/addbook', methods=['GET', 'POST'])
def addBook():
    form = AddBook()
    author_number = ''
    if form.validate_on_submit():
        author = Author.query.filter_by(name=form.author.data).first()
        if author is None:
            author = Author(name=form.author.data)
            db.session.add(author)
            db.session.commit()
        author = form.author.data
        authors = Author.query.all()
        for writer in authors:
            if author == writer.name:
                author_number = writer.id
        book = Book(title=form.title.data,
                    genre=form.genre.data,
                    description=form.description.data,
                    author_id=author_number)
        db.session.add(book)
        db.session.commit()
        flash(form.title.data + " - " + form.author.data + " has been added")
    return render_template('addbook.html', title='Add a Book', form=form)


results = []

@app.route('/import', methods=['GET', 'POST'])
def importBooks():
    api1 = "https://www.googleapis.com/books/v1/volumes?q="
    form = ImportBooks()
    global results
    if form.validate_on_submit() and form.submit.data:
        results = []
        query = "+".join(form.keywords.data.split())
        r = requests.get(api1+query)
        jsonify = json.loads(r.content)
        #print(json.dumps(jsonify, indent=4, sort_keys=True))
        for x in jsonify["items"]:
            results.append({"title":x["volumeInfo"]["title"]})
            try:
                results[-1]["author"] = x["volumeInfo"]["authors"]
            except:
                results[-1]["author"] = "N/A"
            try:
                results[-1]["description"] = x["volumeInfo"]["description"]
            except:
                results[-1]["description"] = "N/A"
            try:
                results[-1]["genre"] = x["volumeInfo"]["categories"]
            except:
                results[-1]["genre"] = "N/A"

        print(results)
    if request.method == "POST" and form.move.data:
        print(results)
        for x in range(9):
            print(request.form.get(str(x)))
        data = request.form.getlist("checkbox")
        for x in data:
            flash(results[int(x)]["title"] + " - " + str(results[int(x)]["author"]) + " has been imported")
            author = Author.query.filter_by(name=results[int(x)]["author"][0]).first()
            if author is None:
                author = Author(name=results[int(x)]["author"][0])
                db.session.add(author)
                db.session.commit()
            author_number = ''
            author = results[int(x)]["author"][0]
            authors = Author.query.all()
            print(author)
            for writer in authors:
                if author == writer.name:
                    author_number = writer.id
            book = Book(title=results[int(x)]["title"],
            author_id=author_number,
            description=results[int(x)]["description"],
            genre=results[int(x)]["genre"][0])
            db.session.add(book)
            db.session.commit()
        print("click")
        results = []
    return render_template('import.html', title='Import Books', form=form, results=results)
