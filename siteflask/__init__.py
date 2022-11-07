from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SECRET_KEY'] = 'e2f8274d48dc01d27c9ab6b844109580' #temporario
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitef.db'

database = SQLAlchemy(app)

from siteflask import routes