import os
DEBUG = True


SQLALCHEMY_DATABASE_URI = "mysql+pymysql://liaowenhao:kcr01260@localhost:3306/elanhome"
#mysql+pymysql://root:kcr01260@localhost:32777/elanhome
#mysql+pymysql://liaowenhao:kcr01260@localhost:3306/elanhome
SECRET_KEY = os.urandom(20)
SQLALCHEMY_TRACK_MODIFICATIONS = True
