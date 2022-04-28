import os

class Config(object):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'
    SESSION_COOKIE_SECURE = True
    BOOTSTRAP_BOOTSWATCH_THEME = 'Simplex'
    DB_DIR = os.getenv('DB_DIR','database')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR,'..', DB_DIR, "db2.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER =  os.getenv('UPLOAD_FOLDER', os.path.join(BASE_DIR,'..' , 'uploads'))
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY','NOKEY')
    LOG_DIR =  os.path.join(BASE_DIR, '../logs')
    MAIL_SERVER = os.getenv('MAIL_SERVER','smtp.mailtrap.io')
    MAIL_PORT = 2525
    MAIL_USERNAME = os.getenv('MAIL_USERNAME','NOKEY')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD','NOKEY')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER','noreply@myapp.com')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SESSION_COOKIE_SECURE = False
    DEBUG = True

