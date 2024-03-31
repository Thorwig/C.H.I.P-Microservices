from flask import Flask, request, jsonify
from model.assistant import ask_assistant

app = Flask(__name__)


@app.route('/assistant', methods=['POST'])
def assistant():
    message = request.json['message']
    response = ask_assistant(message)
    return response.choices[0].message.content
