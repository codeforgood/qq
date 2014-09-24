__author__ = 'sravi'

from flask.ext import restful
from datetime import timedelta
from offload import async, sched_in, get_tasks_scheduled

from qq.tasks.task import count_words_at_url, query_postgres


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
        tasks_scheduled = get_tasks_scheduled()
        return {'tasks_count': len(tasks_scheduled)}


class QueryTask(restful.Resource):
    def get(self):
        task = async(func=query_postgres, params=('select * from qq;',))
        return {'query_result_tracker': task.key}
