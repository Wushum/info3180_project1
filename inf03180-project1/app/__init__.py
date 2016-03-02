from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@localhost/info3180'
app.config['UPLOAD_FOLDER'] = 'static'
db = SQLAlchemy(app)

from app import views, models