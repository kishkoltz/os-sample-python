from wsgi import application, db
from app.models import Author, Book

@application.shell_context_processor
def make_shell_context():
    return {'db': db, 'Author': Author, "Book":Book}

print("books.py loaded")
