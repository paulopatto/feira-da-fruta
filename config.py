import os

_basedir = os.path.abspath(os.path.dirname(__file__))

# Base file in https://github.com/mjhea0/flask-tracking/blob/master/config.py
class DefaultConfiguration(Object):
    DEBUG = False
    TESTING = False

