__author__ = 'sravi'

from server import api
from views.views import *

api.add_resource(HelloWorld, '/now')
api.add_resource(HelloLater, '/later')
api.add_resource(ScheduledQueue, '/tasks')
api.add_resource(QueryTask, '/query')
