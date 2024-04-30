from flask import Blueprint, request, jsonify
from flask_socketio import emit
from ..run import socketio
from .model.stt import transcribe_audio

api_bp = Blueprint('api_bp', __name__)


@api_bp.route('/', methods=['GET'])
def index():
    return "HELLO WORLD, sttService"

@api_bp.route('/stt', methods=['POST'])
def stt():
    message = request.json['message']
    response = transcribe_audio(message)
    return jsonify({"audio_url": f"/audio/{response.id}"})


@socketio.on('message')
def handle_message(message):
    app.logger.info('Received message')
    # Process audio data here
    transcription = transcribe_audio(message)
    emit('transcription', {'text': transcription})


@socketio.on('transcribe', namespace='/stt')
def transcribe(message):
    response = transcribe_audio(message['audio'])
    emit('transcribe', {"audio_url": f"/audio/{response.id}"})
