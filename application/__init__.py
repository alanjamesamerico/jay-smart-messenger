__version__ = '1.0'
from bottle import Bottle

app = Bottle()

from application.controllers import *
