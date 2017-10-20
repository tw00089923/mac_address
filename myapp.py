from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)
Bootstrap(app)


from route import *


if __name__ == '__main__':
    app.run()