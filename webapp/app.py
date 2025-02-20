import asyncio
import requests
from flask import Flask, jsonify, render_template, request
# from multiprocessing import Process, Queue

app = Flask(__name__)

MS_URL = "http://localhost:8000/signal/" # microservice url

def send_signal(signal):
    url = MS_URL + signal
    response = requests.get(url)
    return response
   
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/click-button', methods=['POST'])
def click_button():
    data = request.json # get the data from a page
    signal = data.get('signal')
    response = send_signal(signal) # send signal to the bus!
    return jsonify({"response": f"{response}"})

def main():
    app.run(debug=True, use_reloader=False)

if __name__ == '__main__':
    main()
