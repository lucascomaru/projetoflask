from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)


app.config['SECRET_KEY'] = 'e2f8274d48dc01d27c9ab6b844109580' #temporario
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitef.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from siteflask import routes