from flask import render_template, request, flash, url_for, session, redirect
from myapp import app, login_manager, db
from forms import Mac_address, Users, Create_mac
from models import data, Userdb
from flask_login import login_required,login_user,logout_user
import datetime


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


@app.route('/work_order',methods=['POST','GET'])
def work_order():
    form = Create_mac()
    if request.method == "POST" and form.validate():
        work_number =  request.form['work_order_number']
        return redirect(url_for('mac_add',work_order=work_number))

    return render_template('work_order.html',form=form)

@app.route('/<string:work_order>/list',methods=['GET', 'POST'])
def mac_add(work_order):
    form = Mac_address()
    Mac_db = data()
    index = Mac_db.query.filter_by(work_order=work_order).all()
    print(len(index))
    form.pollet_index.data= int(1+len(index)/40)

    print(form.pollet_index.data)
    form.work_order.data= work_order
    form.date.data = datetime.datetime.now()
    message = {}

    if request.method == "POST" and form.validate():
        mac_address = request.form['mac_address']
        mac = Mac_db.query.filter_by(mac_address=mac_address).first()
        if not mac: 
            pollet_index = request.form['pollet_index']
            date = request.form['date']
            work_order = request.form['work_order']
            datetime_format =datetime.datetime.strftime(datetime.datetime.now(), '%Y/%m/%d')
            mac_data = data(date=datetime_format,mac_address=mac_address,pollet_index=pollet_index,work_order=work_order)
            db.session.add(mac_data)
            db.session.commit()
            message["text"] = "新增成功!"
            message["color"] = "success"
            form.mac_address.data = None
        else:
            message["text"] = "資料庫有重複值" 
            message["color"] = "danger"
    if request.method == "GET":
        print("Reload")


    return render_template('mac_add.html',form=form,message=message,query_data=index)