import os
import json

from flask import Flask, request, Response, Blueprint
from flask import render_template, send_from_directory, url_for

app = Flask(__name__)
app.config.from_object('AngularFlask.Settings')

app.url_map.strict_slashes = False

from AngularFlask.Controllers import indexController, tagController
app.register_blueprint(indexController)
app.register_blueprint(tagController)
