from flask import Blueprint, request
import json

exampleAPIController = Blueprint('exampleAPIController', __name__)


@exampleAPIController.route('/api/ExampleAPIGetWithArgument', methods=['GET'])
def ExampleAPIGetWithArgument():
    argument = str(request.args.get('argument'))
    if not argument:
        abort(400)
    return json.dumps({'result': argument}), 200

@exampleAPIController.route('/api/ExampleAPIGET', methods=['GET'])
def ExampleAPIGET():
    return json.dumps({"result": "success"}), 200

@exampleAPIController.route('/api/ExampleAPIPOST', methods=['POST'])
def ExampleAPIPOST():
    if not request.json or not 'value' in request.json:
        abort(400)
    return json.dumps({"result": request.json.get('value')}), 200
