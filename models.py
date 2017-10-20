from myapp import db

class User(db.Model):
    #__table__name = 'user'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)

class Mac_address(db.Model):
    __table__name = data
    data_id = db.Column(db.integer,primary_key=True)
    date = db.Column(db.DateTime,nullable=False)
    mac_address = db.Column(db.String(8),nullable=False)
    pollet_index = db.Column(db.intger,nullable=False)
    work_order = db.Column(db.String(10))
