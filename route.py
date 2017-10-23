from flask import render_template, request, flash, url_for, session
from myapp import app, login_manager
from forms import Mac_address,Users
from models import data,Userdb
from flask_login import login_required



@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    if session['username'] == None:
        flash('你需要帳戶登錄')
    return render_template('/login.html')

@app.route('/')
def index():
    form = Mac_address()
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    form = Users()
    userdb = Userdb()
    if request.method == "POST":
        user = userdb.query.filter_by(username=form.username).first()

    return render_template('login.html',form=form)


@app.route('/read_mac')
@app.route('/read_mac/<int:page>')
def read_mac_list(page=1):
    data_from_db = data.query.paginate(page=page,per_page=40)
    return render_template('read_mac.html',data = data_from_db )
@app.route('/read_mac/edit/<int:index>')
def edit_mac(index):
    mac_edit = data.query.filterby(index)
    return render_template('mac_edit.html')
