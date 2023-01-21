from flask import Flask, url_for
from flask_bootstrap import Bootstrap
from config import Config

app=Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)

from app import routes

