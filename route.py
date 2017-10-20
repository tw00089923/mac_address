from flask import render_template,request
from myapp import app
from forms import Mac_address,Users
from models import data

@app.route('/')
def index():
    form = Mac_address()
    return render_template('index.html',form = form)

@app.route('/login',methods=['POST','GET'])
def login(user,pwd):
    form = Users()
    if request.methods == "POST":
        return render_template('login.html')
    else:
        return render_template('404.html')
    return render_template('login.html',form = form)


@app.route('/read_mac')
@app.route('/read_mac/<int:page>')
def read_mac_list(page=1):
    form = data.query.paginate(page=page,per_page=40)
    return render_template('read_mac.html',data = form )
@app.route('/read_mac/edit/<int:index>')
def edit_mac(index):
    mac_edit = data.query.filterby(index)
    return render_template('mac_edit.html')
