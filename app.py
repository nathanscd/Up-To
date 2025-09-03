from flask import Flask
from extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'sua_chave_secreta'

# Inicializa extensões
db.init_app(app)

# Importa rotas e modelos depois do init_app
from models import User, Activity, Event
import routes  # arquivo onde você pode separar as rotas
