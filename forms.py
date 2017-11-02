from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, TextField, PasswordField, IntegerField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Length


class Users(FlaskForm):
    username = TextField('使用者帳號',[DataRequired()])
    password = PasswordField('密碼登入',[DataRequired()])
    remember_me = BooleanField('記住我', default=False)


class Mac_address(FlaskForm):
    #data_id = 
    date = DateTimeField('start',[DataRequired()])
    mac_address = StringField('Mac_address')
    pollet_index = IntegerField('盤數',[NumberRange(min=1,max=99)])
    work_order = StringField('工單號碼')


class Create_mac(FlaskForm):
    work_order_number = TextField('工單號碼',[DataRequired(),Length(max=7)])