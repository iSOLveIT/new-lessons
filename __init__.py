"""
    File used to initialise Flask and Flask extensions
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://randy:Password#1234@localhost/new_lessons'
# postgresql+psycopg2://isolveit:pswd#1234@localhost:8432/traveller
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrateDB = Migrate(app, db)


from . import route
