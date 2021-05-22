from flask import Flask
from flask_rq2 import RQ
import requests

app = Flask(__name__)
app.config['RQ_REDIS_URL'] = 'redis://127.0.0.1:6379/0'
rq = RQ(app)


@rq.job
def add():
    res = requests.post("http://localhost:8080/test")
    if res.status_code == 200:
        print(res.json())

@app.route('/', methods=['GET'])
def index():
    job = add.queue()
    return "ok"
