from flask import Flask, url_for
from flask_bootstrap import Bootstrap





app=Flask(__name__)


Bootstrap(app)



from app import routes

