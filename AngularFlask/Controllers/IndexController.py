import os
import glob

from flask import Blueprint, render_template
indexController = Blueprint('indexController', __name__)

@indexController.route('/')
def CallIndexController():
    jsImports = {
        "services":[],
        "directives":[],
        "controllers":[]
    }

    for service in glob.glob(os.path.join(os.getcwd(), 'AngularFlask', 'static', 'js', 'services', '*.js')):
        jsImports['services'].append(os.path.basename(service))
    for controller in glob.glob(os.path.join(os.getcwd(), 'AngularFlask', 'static', 'js', 'controllers', '*.js')):
        jsImports['controllers'].append(os.path.basename(controller))
    for directive in glob.glob(os.path.join(os.getcwd(), 'AngularFlask', 'static', 'js', 'directives', '*.js')):
        jsImports['directives'].append(os.path.basename(directive))


    return render_template('index.html', data=jsImports)
