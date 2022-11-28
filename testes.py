from siteflask import app, database
from siteflask.models import Usuario, Post

#with app.app_context():
#    database.create_all()

with app.app_context():
    database.create_all()

