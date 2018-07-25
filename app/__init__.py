from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
sio = SocketIO(app, async_mode='eventlet')

app.config.from_object('config.Config')
from . import views
