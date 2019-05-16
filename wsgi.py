from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

application = Flask(__name__)
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)



if __name__ == "__main__":
    application.run()
    print("application.run()")

@application.shell_context_processor
def make_shell_context():
    return {'db': db, 'Author': Author, "Book":Book}

    
from app.models import Author, Book
