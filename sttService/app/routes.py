from flask import Blueprint, request, jsonify
from .model.stt import transcribe_audio

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/stt', methods=['POST'])
def stt():
    message = request.json['message']
    response = transcribe_audio(message)
    return jsonify({"audio_url": f"/audio/{response.id}"})
