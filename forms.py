from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, TextField, PasswordField, IntegerField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Length, Regexp


class Users(FlaskForm):
    username = TextField('使用者帳號',[DataRequired(message="密碼不可以空白")])
    password = PasswordField('密碼登入',[DataRequired(message="密碼不可以空白")])
    remember_me = BooleanField('記住我', default=False)


class Mac_address(FlaskForm):
    #data_id = 
    date = DateTimeField('時間',[DataRequired(message="日期不可以空白")])
    mac_address = StringField('Mac_address',[Regexp("[0-9A-F]{2}\-[0-9A-F]{2}\-[0-9A-F]{2}",message="格式錯誤[舉例 : 0D-01-A1 16進為格式] "), Length(min=8,max=8,message="【Mac】字數不對!")])
    pollet_index = IntegerField('盤數',[DataRequired(message="盤數不可以空白"),NumberRange(min=1,max=99,message="數字1-99盤")])
    work_order = StringField('工單號碼',[ DataRequired(), Length(min=8,max=8,message="字數不對!"), Regexp("^[A|B|D|R|J]\d{7}",message="格式錯誤[舉例 : A1712254] ")])


class Create_mac(FlaskForm):
    work_order_number = StringField('工單號碼',[ DataRequired(), Length(min=8,max=8,message="字數不對!"), Regexp("^[A|B|D|R|J]\d{7}",message="格式錯誤[舉例 : A1712254] ")])