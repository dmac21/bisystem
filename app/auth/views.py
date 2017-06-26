from . import auth
from .forms import LoginForm
from flask import render_template,redirect,url_for,request
from flask_login import login_user,logout_user,login_required,current_user
from ..models import  User

@auth.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.account.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('auth/login.html',form=form)