#coding:utf-8
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length

class LoginForm(Form):
    account=StringField(validators=[Required(u'用户名不能为空！'),Length(1,64)],render_kw={"placeholder": u'请输入你的用户名'})
    password=PasswordField(validators=[Required(u'密码不能为空！')],render_kw={"placeholder": u'请输入你的密码'})
    remember_me = BooleanField(u'保持登录')
    submit=SubmitField(u'登录')