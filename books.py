from app import application, db
from app.models import Author, Book

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Author': Author, "Book":Book}
