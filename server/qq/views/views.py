__author__ = 'sravi'

from qq.server import qq, sq, app
from qq.tasks.task import count_words_at_url
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
        task = sq.enqueue_in(timedelta(minutes=1), count_words_at_url, 'http://nvie.com')
        return {'later': task.key}


class ScheduledQueue(restful.Resource):
    def get(self):
        tasks_scheduled = sq.get_jobs()
        print tasks_scheduled
        print app.config.get('DATABASE')
        return {'tasks_count': len(tasks_scheduled)}
