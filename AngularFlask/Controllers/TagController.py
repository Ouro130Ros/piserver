from flask import Blueprint, request
import json
import os

from DataAccess import TagRepository

tagController = Blueprint('tagController', __name__)

@tagController.route('/api/Tags/List', methods=['GET'])
def ListTags():
    tagRepo = TagRepository(os.path.join(os.getcwd(), 'boardgames.db'))
    result = tagRepo.GetTags()
    print result
    return result, 200

@tagController.route('/api/Tags/Add', methods=["POST"])
def AddTag():
    print request
    print request.form
    if not request.form or not 'tagName' in request.form or not 'tagType' in request.form:
        return "FAIL", 400
    tagRepo = TagRepository(os.path.join(os.getcwd(), 'boardgames.db')) 
    tagRepo.AddTag(request.form['tagName'], request.form['tagType'])
    return "OK", 200

