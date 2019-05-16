from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    books = db.relationship('Book', backref='writer', lazy='dynamic')

    def __repr__(self):
        return '<{}>'.format(self.name)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    genre = db.Column(db.String(64))
    description = db.Column(db.String())
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return '<{}>'.format(self.title)
