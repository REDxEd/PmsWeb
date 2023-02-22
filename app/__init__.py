from flask import Flask, url_for
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app=Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view='login'

# instancia do bd--------------------------------------------------->
db=SQLAlchemy(app)
Migrate = Migrate(app,db)

# models define a estrutura do banco de dados
from app import routes,models

