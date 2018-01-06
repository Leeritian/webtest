from flask import Flask, render_template, request, make_response, flash,\
                 url_for
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from model import User, session
import hashlib
import datetime
from functool import is_logined,is_log

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if is_log():
        return "您已经登录了"

    if request.method == "POST":
        account = request.form['account']
        password = request.form['password']        
        user = session.query(User).filter_by(account=account).first()
        if user is not None and user.verify_password(password):
            response = make_response(render_template('index.html'))
            response.set_cookie('account',account,\
                                expires=datetime.datetime.today()+datetime.timedelta(days=14))
            response.set_cookie('checksum',hashlib.md5(account.encode()).hexdigest(),expires=datetime.datetime.today()+datetime.timedelta(days=14))
            return response
        flash('Invalid username or password.')
    else:
        return render_template('auth.html')

@app.route('/logout')
def logout():
    response= make_response(render_template('index.html'))   #该做个跳转页面吗
    response.delete_cookie("account")
    response.delete_cookie("checksum")
    return response


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "POST":
        account = request.form['account']
        user = session.query(User).filter_by(account=account).first()
        if user is not None:
            return "该帐号已经被注册了"
        password = request.form['password']
        name = request.form['name']
        user = User(account=account,password=password,name=None)
        session.add(user)
        session.commit()
        return "注册成功"
    else:
        return render_template('register.html')
            
'''
@app.route('/register', method=['GET','POST'])
def register():
'''
app.run(debug=True)
