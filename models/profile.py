from google.appengine.ext import ndb

class Profile(ndb.Model):
    photo = ndb.StringProperty(indexed=False)
    photo_key = ndb.StringProperty(indexed=True)
    user_id = ndb.StringProperty(indexed=True)
    username = ndb.StringProperty(indexed=True)
    first_name = ndb.StringProperty(indexed=True)
    last_name = ndb.StringProperty(indexed=True)
    twitter = ndb.StringProperty(indexed=True)