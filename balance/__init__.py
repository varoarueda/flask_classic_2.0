from flask import Flask

# Crear la app
app = Flask(__name__)

from balance.views import *

