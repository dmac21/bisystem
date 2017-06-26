import os
from app import create_app
from flask.ext.script import Manager

app=create_app(os.getenv('FLASK_CONFIG') or 'default')
manager=Manager(app)

#在shell中绑定app,db,User,Role
def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role,Permission=Permission)

#绑定shell命令
manager.add_command("shell",Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()