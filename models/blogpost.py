from google.appengine.ext import ndb

# Object represents a diary entry
class Blogpost(ndb.Model):
    title= ndb.StringProperty(indexed=True)
    post = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
    photo = ndb.BlobProperty(indexed=False)
    photo_key = ndb.StringProperty(indexed=True)
    date_text = ndb.StringProperty(indexed=False)
    user_id = ndb.StringProperty(indexed=True)