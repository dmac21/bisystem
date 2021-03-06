import os
from app import create_app,db
from flask.ext.script import Manager,Shell,Server
from app.models import User,Role

app=create_app(os.getenv('FLASK_CONFIG') or 'default')
manager=Manager(app)


def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role)


manager.add_command("shell",Shell(make_context=make_shell_context))

manager.add_command("runserver", Server(host="127.0.0.1", port=5000, use_debugger=True))


if __name__ == '__main__':
    manager.run()