from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(debug=True):
    app = Flask(__name__)
    app.debug = debug

    from .routes import api_bp
    app.register_blueprint(api_bp)

    socketio.init_app(app)
    return app
