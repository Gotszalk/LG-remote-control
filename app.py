import asyncio
from flask import Flask, jsonify, render_template, request
from multiprocessing import Process, Queue
from lib.subproc import initiate 

app = Flask(__name__)
   
remote_bus = Queue() # bus to send the signals!

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/click-button', methods=['POST'])
def click_button():
    data = request.json # get the data from a page
    signal = data.get('signal')
    remote_bus.put(signal) # send signal to the bus!
    return jsonify({"response": f"Received {signal}!"})

if __name__ == '__main__':
    remote = Process(target=initiate, args=(remote_bus,)) # create subprocess to deal with signals
    # remote.daemon = True
    remote.start()
    # remote.join()

    app.run(debug=True, use_reloader=False, host='127.0.0.1', port=5010)
