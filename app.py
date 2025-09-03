from flask import Flask
from extensions import db
from models import User, Activity, Event


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'sua_chave_secreta'

db.init_app(app)
import routes 