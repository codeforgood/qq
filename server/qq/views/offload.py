__author__ = 'sravi'

from qq.server import qq, sq
from flask import current_app as app


def async(func, params, result_ttl=500):
    task = qq.enqueue_call(func=func,
                           args=params + (app.config,),
                           result_ttl=result_ttl)
    return task


def sched_in(func, params, timedelta):
    task = sq.enqueue_in(timedelta, func, params, config=app.config)
    return task


def get_tasks_scheduled():
    return sq.get_jobs()
