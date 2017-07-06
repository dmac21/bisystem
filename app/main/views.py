from . import main
from flask import render_template
from flask_login import login_required, current_user

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/wechat')
def wechat():
    return render_template('wechat.html')

@main.route('/sysmanage')
def sysmanage():
    return render_template('sysmanage.html')