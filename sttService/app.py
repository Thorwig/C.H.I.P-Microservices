from flask import Flask, request, jsonify
from model.stt import transcribe_audio

app = Flask(__name__)


@app.route('/tts', methods=['POST'])
def stt():
    message = request.json['message']
    response = transcribe_audio(message)
    return jsonify({"audio_url": f"/audio/{response.id}"})


if __name__ == '__main__':
    app.debug = True
    app.run(port=2003)
