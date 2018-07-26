from . import app, sio
from flask import render_template
from flask_socketio import emit
from time import strftime
from app.ds18b20 import read_temp

thread = None


def background_thread():
    while True:
        result = read_temp()[0]
        sio.sleep(1)
        sio.emit('my_response', {'temp': result}, namespace='/test')

@app.route('/')
def home():
    return render_template('index.html', title='My page')

@sio.on('connect', namespace='/test')
def test_connect():
    global thread
    if thread is None:
        thread = sio.start_background_task(target=background_thread)
    emit('my_response', {'temp': ''})


