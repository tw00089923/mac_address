from flask_wtf import FlaskForm
from wtforms import StringField, DateTimefield, TextField, PasswordField
from wtforms.validators import DataRequired


class User(FlaskForm):
    username = TextField('username')
    password = PasswordField('password')


class Mac_address(FlaskForm):
    data_id = 
    date = 
    mac_address = 
    pollet_index = 
    work_order = 