from flask import Flask, request, jsonify
from model.assistant import ask_assistant

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return "HELLO WORLD"


@app.route('/assistant', methods=['POST'])
def assistant():
    message = request.json['message']
    response = ask_assistant(message)
    return response.choices[0].message.content


if __name__ == '__main__':
    app.debug = True
    app.run(port=2002)
