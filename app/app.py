from flask import Flask
from flask_rq2 import RQ
import requests

app = Flask(__name__)
app.config['RQ_REDIS_URL'] = 'redis://redis:6379/0'
rq = RQ(app)


@rq.job
def add():
    res = requests.post("http://172.18.0.2:8080/test")  # Ip from external docker network
    if res.status_code == 200:
        print(res.text)
        with open("ggout.txt", "a") as f:
            f.write(res.text+"\n")
        return res.json()

@app.route('/', methods=['GET'])
def index():
    job = add.queue()
    return "ok"
