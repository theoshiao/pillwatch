from flask import Flask
from flask import render_template
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/api/time")
def get_current_time():
    print('testing that endpoint was hit');
    return {'time': time.time()}