__author__ = 'sravi'

from server import api, qq
from tasks.task import count_words_at_url
from flask.ext import restful


class HelloWorld(restful.Resource):
    def get(self):
        task = qq.enqueue(count_words_at_url, 'http://nvie.com')
        return {'hello': task.key}

api.add_resource(HelloWorld, '/')
