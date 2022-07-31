import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '1q2w3e4r'
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com') 
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587')) 
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
         ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') 

    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]' 
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>' 
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = \
            os.getenv('DEV_DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = \
            os.getenv('DEV_DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'tests', 'data-test.sqlite')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = \
            os.getenv('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'dev': DevConfig,
    'test': TestConfig,
    'prod': ProdConfig,
    'default': DevConfig
}
