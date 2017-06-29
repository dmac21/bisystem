#coding:utf-8
from . import auth
from .forms import LoginForm
from flask import render_template,redirect,url_for,request,flash
from flask_login import login_user,logout_user,login_required,current_user
from ..models import  User

@auth.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash(u'无效的用户名或者密码')
    return render_template('auth/login.html',form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'你已成功退出系统')
    return redirect(url_for('main.index'))