__author__ = 'sravi'

import os

from flask import Flask
from flask_environments import Environments
from flask.ext import restful
from flask.ext.bcrypt import Bcrypt
from flask.ext.httpauth import HTTPBasicAuth
from redis import Redis
from rq import Queue
from rq_dashboard import RQDashboard
from rq_scheduler import Scheduler

basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../')

app = Flask(__name__)
RQDashboard(app)
env = Environments(app)
env.from_yaml(os.path.join(os.getcwd(), 'qq', 'config.yml'))

# flask-restful
api = restful.Api(app)

# flask-bcrypt
flask_bcrypt = Bcrypt(app)

# flask-httpauth
auth = HTTPBasicAuth()

# redis-queue
qq = Queue(connection=Redis())
sq = Scheduler(connection=Redis())

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

import routes
