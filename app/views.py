from . import app, sio
from flask import render_template
from flask_socketio import emit
from time import strftime


thread = None


def background_thread():
    count = 0
    while True:
        sio.sleep(1)
        count += 1
        sio.emit('my_response', {'data': 'Message from server', 'count': count}, namespace='/test')

@app.route('/')
def home():
    return render_template('index.html', title='My page')


@sio.on('connect', namespace='/test')
def test_connect():
    global thread
    if thread is None:
        thread = sio.start_background_task(target=background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})
