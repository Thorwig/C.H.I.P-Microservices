from flask import Flask, request, jsonify
from model.tts import get_audio

app = Flask(__name__)


@app.route('/tts', methods=['POST'])
def tts():
    message = request.json['message']
    response = get_audio(message)
    return jsonify({"audio_url": f"/audio/{response.id}"})
