from flask import Flask, request, jsonify
from model.tts import get_audio

app = Flask(__name__)


@app.route('/tts', methods=['POST'])
def tts():
    message = request.json['message']
    response = get_audio(message)
    return jsonify({"audio_url": f"/audio/{response.id}"})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=2004)
