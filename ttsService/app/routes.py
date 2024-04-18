from flask import Blueprint, request, jsonify
from .model.tts import get_audio

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/tts', methods=['POST'])
def tts():
    message = request.json['message']
    response = get_audio(message)
    return jsonify({"audio_url": f"/audio/{response.id}"})
