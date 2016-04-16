#!/usr/bin/python

from flask import Flask
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)

#get scss
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('scss/main.scss', filters='pyscss', output='css/all.css')
assets.register('scss_all', scss)

app.config.from_object('config')

from app import views