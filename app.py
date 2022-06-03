from flask import Flask, render_template, request, flash
from threading import Thread
from flask_socketio import SocketIO
import time
import mq135adc


app = Flask(__name__,
            static_folder='static',
            template_folder='templates')
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

def luft_test():
    while True: 
        time.sleep(10.0)
        socketio.emit('luftkvalitet', mq135adc.air_quality())
        
luft_thread = Thread(target=luft_test)
luft_thread.start()

if __name__ == '__main__':
    socketio.run(app, port="8000", host="0.0.0.0", debug=True)