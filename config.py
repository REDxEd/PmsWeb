import os

class Config(object):
    # A SECRET_KEY aqui serve principalmente para evitar Cross-Site Request Forgery
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'