from flask import Flask
from database import banco

app = Flask(__name__)


from routes import routes


if __name__ == "__main__":
    app.run(debug=True)