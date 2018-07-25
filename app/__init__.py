from pyA20.gpio import gpio
from pyA20.gpio import port
from app.dht11 import DHT11
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
sio = SocketIO(app, async_mode='eventlet')

PIN2 = port.PA6
gpio.init()


dht_data = DHT11(pin=PIN2)

app.config.from_object('config.Config')

from . import views

