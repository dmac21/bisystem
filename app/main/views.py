#coding:utf-8
from . import main
from flask import render_template
from flask_login import login_required, current_user
import MySQLdb as mysql
import json,datetime

database=mysql.connect(user='root',passwd='root',db='wechat_data2',charset='utf8')
cursor=database.cursor()


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/wechat')
def wechat():
    sql="select ref_date,sum(cumulate_user) cumulate_user from usercumulate_data where ref_date>='2017-05-01' group by ref_date"
    sql2="select charge_team ,count(*) wechats from  account_data group by charge_team"
    cursor.execute(sql)
    data =cursor.fetchall()
    cursor.execute(sql2)
    data2=cursor.fetchall()
    jsonstr={}
    jsonstr2={}
    jsonstr2['charge_team']=[x[0] for x in data2]
    jsonstr2['wechats'] = [int(x[1]) for x in data2]
    jsonstr['ref_date']=[x[0].strftime('%Y-%m-%d') for x in data]
    jsonstr['cumulate_user'] = [int(x[1]) for x in data]
    return render_template('wechat.html',data=jsonstr,data2=jsonstr2,data3=data)

@main.route('/sysmanage')
def sysmanage():
    return render_template('sysmanage.html')