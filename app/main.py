from flask import Flask
from flask_rq2 import RQ
import requests

app = Flask(__name__)
app.config['RQ_REDIS_URL'] = 'redis://redis:6379/0'
rq = RQ(app)


@rq.job
def add():
    res = requests.post("http://0.0.0.0:8080/test")
    if res.status_code == 200:
        print(res.json())

@app.route('/', methods=['GET'])
def index():
    job = add.queue()
    return "ok"
