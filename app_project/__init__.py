__version__ = '1.0'
from bottle import Bottle

app = Bottle()

from app_project.controllers import *
