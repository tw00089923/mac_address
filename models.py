from myapp import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Userdb(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    password = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    #@property
    #def password(self):
        #raise AttributeError('password is not a readable attribute')
    #@password.setter
    #def password(self, password):
        #self.password_hash = generate_password_hash(password)
    def __repr__(self):
        return '<User %r>' % self.name
    
    
class data(db.Model):
    __tablename__ = "data"
    data_id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.DateTime,nullable=False)
    mac_address = db.Column(db.String(8),nullable=False)
    pollet_index = db.Column(db.Integer,nullable=False)
    work_order = db.Column(db.String(10))
