from google.appengine.ext import ndb

__author__ = 'yasith'


class App:
    DEFAULT_KEY = ndb.Key('KEY', "DEFAULT_KEY")
    session = {}