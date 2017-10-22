from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)
manager.add_command('runserver', Server())
Bootstrap(app)

from route import *


if __name__ == '__main__':
    app.run()