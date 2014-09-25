__author__ = 'sravi'

from flask.ext.restful import Resource, reqparse, abort
from datetime import timedelta
from offload import async, sched_in, get_tasks_scheduled
from qq.server import auth
from qq.tasks.task import count_words_at_url, query_postgres


class HelloWorld(Resource):
    def get(self):
        task = async(func=count_words_at_url, params=('http://nvie.com',),)
        return {'hello': task.key}


class HelloLater(Resource):
    def get(self):
        task = sched_in(func=count_words_at_url, params='http://nvie.com', timedelta=timedelta(minutes=1))
        return {'later': task.key}


class ScheduledQueue(Resource):
    def get(self):
        tasks_scheduled = get_tasks_scheduled()
        return {'tasks_count': len(tasks_scheduled)}


class QueryTask(Resource):
    decorators = [auth.login_required]

    parser = reqparse.RequestParser()
    parser.add_argument('query', type=str, required=True, help="query cannot be blank!")

    def get(self):
        return {'ping': 'pong'}, 200

    def post(self):
        args = QueryTask.parser.parse_args()
        task = async(func=query_postgres, params=(args['query'],))
        return {'query_tracker': task.key}, 201
