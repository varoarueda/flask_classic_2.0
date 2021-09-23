from flask import Flask

# Crear la app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")

from balance.views import *

