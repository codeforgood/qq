__author__ = 'sravi'

from server import api, qq, sq
from tasks.task import count_words_at_url
from flask.ext import restful
from datetime import timedelta


class HelloWorld(restful.Resource):
    def get(self):
        task = qq.enqueue_call(func=count_words_at_url,
                               args=('http://nvie.com',),
                               result_ttl=500)
        return {'hello': task.key}


class HelloLater(restful.Resource):
    def get(self):
        task = sq.enqueue_in(timedelta(minutes=1), count_words_at_url, ('http://nvie.com',))
        return {'later': task.key}


api.add_resource(HelloWorld, '/')
api.add_resource(HelloLater, '/later')
