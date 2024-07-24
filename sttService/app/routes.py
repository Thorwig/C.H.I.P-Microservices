from flask import Blueprint, request, jsonify
from flask_socketio import emit
from ..run import socketio
from .model.stt import transcribe_audio

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/', methods=['GET'])
def index():
    return "HELLO WORLD, sttService"


@socketio.on('transcribe', namespace='/stt')
def transcribe(message):
    print('Transcribe event received')
    response = transcribe_audio(message['audio'])
    emit('transcribe', {"audio_url": f"/audio/{response.id}"})
    print('Transcribe event sent')
