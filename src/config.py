# module configurations
import os

# get the folder where the script runs
_basedir = os.path.abspath(os.path.dirname(__file__))

# dev environment, enable flask error page for when an error occurs
DEBUG = True

ADMINS = frozenset(['email@email.com'])

# used to sign cookies
SECRET_KEY = 'shhh'

# db connection options .. todo
SQLALCHEMY_DATABASE_URI = 'postgresql://vagrant:vagrant@192.168.50.18:5432/hcm'
DATABASE_CONNECT_OPTIONS = {}

# THREADS_PER_PAGE = 8

# protect against form post fraud
CSRF_ENABLED = True
CSRF_SESSION_KEY = "unhackable"
