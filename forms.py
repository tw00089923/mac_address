from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, TextField, PasswordField, IntegerField 
from wtforms.validators import DataRequired


class Users(FlaskForm):
    username = TextField('使用者帳號',[DataRequired()])
    password = PasswordField('密碼登入',[DataRequired()])


class Mac_address(FlaskForm):
    #data_id = 
    date = DateTimeField('start',validators=[DataRequired()])
    mac_address = StringField('Mac_address')
    pollet_index = StringField('第幾盤')
    work_order = StringField('工單號碼')