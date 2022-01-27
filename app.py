from flask import Flask, session,abort
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_login import LoginManager,login_required
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



app = Flask(__name__)


app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
admin = Admin(app, name='MercoStoreAdmin', template_mode='bootstrap3')
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view='/login'
app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'

from routes.views import *


if __name__=="__main__":
    app.run(debug=True)