from flask import render_template, request, flash, url_for, session, redirect, jsonify, json
from myapp import app, login_manager, db
from forms import Mac_address, Users, Create_mac, Update_mac, Query_mac
from models import data, Userdb, modify_data_mac
from flask_login import login_required,login_user,logout_user
import datetime
@login_manager.unauthorized_handler
def unauthorized():
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
    return render_template('read_mac.html',data = data_from_db)
@app.route('/work_order',methods=['POST','GET'])
def work_order():
    form = Create_mac()
    if request.method == "POST" and form.validate():
        work_number =  request.form['work_order_number']
        return redirect(url_for('mac_add',work_order=work_number))
    return render_template('work_order.html',form=form)
@app.route('/<string:work_order>/addlist',methods=['GET', 'POST'])
def mac_add(work_order):
    #初始化 form && Mac_db
    form = Mac_address()
    Mac_db = data()
    #訊息提供前端
    message = {}
    #提供新的Form 資料 更新完頁面後 更新資料

    #print("INITTIAL _ {}".format(form.pollet_index.data))
    form.work_order.data= work_order
    form.date.data = datetime.datetime.now()
  
    
    #接收 Method 方法 
    if request.method == "POST" and form.validate_on_submit():
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
            form.mac_address.data = None
            message = {"text":"新增成功!","color":"success"}
        else:
            message["text"] = "資料庫有重複值" 
            message["color"] = "danger" 
    if request.method == "GET":
        index=Mac_db.query.filter_by(work_order=work_order).all()
        form.pollet_index.data = int(len(index)/40+1)
        print("GET {}".format(len(index))) 
    index=Mac_db.query.filter_by(work_order=work_order).all()
    #寫入json給D3使用
    json_file = json.dumps([i.serialize for i in index])
    return render_template('mac_add.html', form=form, message=message, query_data=index, data_d3=json_file)
@app.route('/readlist',methods=['GET', 'POST'])
def query_mac():
    form = Query_mac()
    #data_from_db = data.query.filter(work_order=work_order)
    if request.method == "POST" and form.validate_on_submit():
        Mac_db = data()
        mac_address =request.form['mac_address']
        index = Mac_db.query.filter_by(mac_address=mac_address).order_by(Mac_db.data_id).first()
        id = index.data_id
        print(id)
        return redirect(url_for('mac_update',id=id))  
    return render_template('query_mac.html',form=form)
@app.route('/readlist/<int:id>/update',methods=['GET', 'POST'])
def mac_update(id):
    Mac_db = data()
    form =  Update_mac()
    index = Mac_db.query.get(id)
    form.old_mac_address.data = index.mac_address
    form.pollet_index.data = index.pollet_index
    form.work_order.data = index.work_order 
    if request.method == "POST" and form.validate_on_submit():
        new_mac_address = request.form['new_mac_address']
        old_mac_address = request.form['old_mac_address']
        work_order = request.form['work_order']
        date = datetime.datetime.now()
        pollet_index =  request.form['pollet_index']
        index.mac_address = new_mac_address 
        index.work_order = work_order
        index.pollet_index = pollet_index
        #db.session.commit()  
        modify_data = modify_data_mac(id=id, new_mac=new_mac_address, old_mac=old_mac_address, date=date )
        db.session.add(modify_data)
        db.session.commit()
        return redirect(url_for('mac_update',form=form))
    return render_template('mac_update.html',form=form)
