from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import logging
from sys import stdout

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(stdout)) # log print
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True # debug mode 활성화
socketio = SocketIO(app)
app.secret_key = '0000'
prediction_global = 999


@socketio.on('connect', namespace='/test')
def test_connect():
    app.logger.info("client connected")


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/result", methods=['POST'])
def result():
    global prediction_global
    return jsonify({'result': prediction_global})


if __name__ == "__main__":
    socketio.run(app)
