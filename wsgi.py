print("WSGI.PY LOADED")
from app import app as application

if __name__ == "__main__":
    application.run()
    print("application.run()")
