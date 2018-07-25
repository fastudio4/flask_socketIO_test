from . import app, sio, dht_data
from flask import render_template
from flask_socketio import emit
from time import strftime


thread = None


def background_thread():
    while True:
        result = dht_data.read()
        sio.sleep(1)
        if result.is_valid():
            sio.emit('my_response', {'data': 'Message from server', 'count': result.temperature}, namespace='/test')

@app.route('/')
def home():
    return render_template('index.html', title='My page')

@sio.on('connect', namespace='/test')
def test_connect():
    global thread
    if thread is None:
        thread = sio.start_background_task(target=background_thread)
    emit('my_response', {'data': 'Connected', 'count': ' '})


