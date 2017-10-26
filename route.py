from flask import render_template, request, flash, url_for, session, redirect
from myapp import app, login_manager
from forms import Mac_address, Users
from models import data, Userdb
from flask_login import login_required,login_user,logout_user



@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    if session['username'] == None:
        flash('你需要帳戶登錄')
    return render_template('/login.html')
@login_manager.user_loader
def load_user(user_id):
    return Userdb.query.get(user_id)

@app.route('/')
def index():
    form = Mac_address()
    return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login():
    error=None
    form = Users()
    userdb = Userdb()
    if request.method == "POST" and form.validate_on_submit():
        user = userdb.query.filter_by(name=request.form["username"]).first()
        if user.password == request.form['password']:
            login_user(user)
            return redirect(url_for('index'))    
    return render_template('login.html',form=form)
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index')) 

@app.route('/read_mac')
@app.route('/read_mac/<int:page>')
def read_mac_list(page=1):
    data_from_db = data.query.paginate(page=page,per_page=40)
    return render_template('read_mac.html',data = data_from_db )
@app.route('/read_mac/edit/<int:index>')
def edit_mac(index):
    mac_edit = data.query.filterby(index)
    return render_template('mac_edit.html')
