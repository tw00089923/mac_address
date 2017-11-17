from myapp import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Userdb(db.Model, UserMixin):
    __tablename__ = "users"
    __table_args__ = {'mysql_engine': 'InnoDB','mysql_charset': 'utf8'}
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
    __table_args__ = {'mysql_engine': 'InnoDB','mysql_charset': 'utf8'}
    data_id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.DateTime,nullable=False)
    mac_address = db.Column(db.String(8),nullable=False)
    pollet_index = db.Column(db.Integer,nullable=False)
    work_order = db.Column(db.String(10))

    #def __init__(self,**kwargs):
        #super(data, self).__init__(**kwargs)
    
    @property
    def serialize(self):
        return {'id':self.data_id,'date':self.date,'mac_address':self.mac_address,'pollet_index':self.pollet_index,'work_order':self.work_order}
    @property
    def serialize_many2many(self):
        return [ item.serialize for item in self.many2many]

class modify_data_mac(db.Model):
    __tablename__ = "modify_data_mac"
    __table_args__ = {'mysql_engine': 'InnoDB','mysql_charset': 'utf8'}
    data_id = db.Column(db.Integer,primary_key=True)
    id = db.Column(db.Integer,nullable=False)
    new_mac = db.Column(db.String(8),nullable=False)
    old_mac = db.Column(db.String(8),nullable=False)
    date = db.Column(db.DateTime,nullable=False)


