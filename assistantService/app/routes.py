from flask import Blueprint, request, jsonify
from .model.assistant import ask_assistant

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/', methods=['GET'])
def hello():
    return "HELLO WORLD"


@api_bp.route('/assistant', methods=['POST'])
def assistant():
    message = request.json['message']
    response = ask_assistant(message)
    return response
