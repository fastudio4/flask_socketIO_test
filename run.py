from app import app, sio

sio.run(app, host='0.0.0.0')
