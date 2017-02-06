from Flask import Blueprint, request
import json
import os

from DataAccess import TagRepository

tagController = Blueprint('tagController', __name__)

@tagController.route('/api/Tags/List', methods=['GET'])
def ListTags():
    tagRepo = TagRepository(os.path.join(os.getcwd(), 'boardgames.db'))
    return json.dumps(tagRepo.GetTags()), 200

@tagController.route('/api/Tags/Add', methods=["POST"])
def AddTag():
    if not request.json or not 'tagName' in request.json or not 'tagType' in request.json:
        abort(400)
    tagRepo = TagRepository(os.path.join(os.getcwd), 'boardgames.db') 
    tagRepo.AddTag(request.json['tagName'], request.json['tagType'])
    return 200
