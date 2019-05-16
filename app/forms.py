from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import Author, Book

class AddBook(FlaskForm):
    author = StringField("Author", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired()])
    genre = StringField("Genre", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    submit = SubmitField('Add')

class ImportBooks(FlaskForm):
    keywords = StringField("Keywords", validators=[DataRequired()])
    submit = SubmitField('Search')
    move = SubmitField('Import')
