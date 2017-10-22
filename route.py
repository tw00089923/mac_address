from flask import render_template, request, flash, url_for, session
from myapp import app, login_manager
from forms import Mac_address,Users
from models import data
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
    return render_template('index.html',form = form)

@app.route('/login',methods=['POST','GET'])
@login_required
def login(user,pwd):
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/read_mac')
@app.route('/read_mac/<int:page>')
@login_required
def read_mac_list(page=1):
    form = data.query.paginate(page=page,per_page=40)
    return render_template('read_mac.html',data = form )
@app.route('/read_mac/edit/<int:index>')
def edit_mac(index):
    mac_edit = data.query.filterby(index)
    return render_template('mac_edit.html')
