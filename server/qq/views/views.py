__author__ = 'sravi'

from flask.ext import restful
from datetime import timedelta
from qq.server import qq, sq
from flask import current_app as app
from qq.tasks.task import count_words_at_url, query_postgres


def async(func, params, result_ttl=500):
    task = qq.enqueue_call(func=func,
                           args=params + (app.config,),
                           result_ttl=result_ttl)
    return task


def sched_in(func, params, timedelta):
    task = sq.enqueue_in(timedelta, func, params, config=app.config)
    return task


class HelloWorld(restful.Resource):
    def get(self):
        task = async(func=count_words_at_url, params=('http://nvie.com',),)
        return {'hello': task.key}


class HelloLater(restful.Resource):
    def get(self):
        task = sched_in(func=count_words_at_url, params='http://nvie.com', timedelta=timedelta(minutes=1))
        return {'later': task.key}


class ScheduledQueue(restful.Resource):
    def get(self):
        tasks_scheduled = sq.get_jobs()
        return {'tasks_count': len(tasks_scheduled)}


class QueryTask(restful.Resource):
    def get(self):
        task = async(func=query_postgres, params=('select * from qq;',))
        return {'query_result_tracker': task.key}
