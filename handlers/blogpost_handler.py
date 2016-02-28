import uuid
import json

from base_handler import Handler
from app import App
from models.blogpost import Blogpost
from page_handler import PageHandler

class BlogpostHandler(Handler):
    def post(self):
        post = self.request.get("post")
        title = self.request.get("title")
        photo = str(self.request.get("photo"))

        user = {'user_id': "user_id"}

        if user:
            invalidFieldFlag = False
            # Check if diary entry or place is invalid
            if len(title.strip()) == 0:
                PageHandler.invalidTitle = True
                invalidFieldFlag = True
            if len(post.strip()) == 0:
                PageHandler.invalidPost = True
                invalidFieldFlag = True
            if len(photo.strip()) < 100:
                PageHandler.invalidPhoto = True
                invalidFieldFlag = True

            if not invalidFieldFlag:
                PageHandler.invalidTitle = PageHandler.invalidPost = PageHandler.invalidPhoto = False

                user_id = user['user_id']
                new_blogpost = Blogpost(parent=App.DEFAULT_KEY)
                new_blogpost.post = post
                new_blogpost.title = title
                new_blogpost.photo = photo
                new_blogpost.photo_key = uuid.uuid4().hex
                new_blogpost.user_id = user_id


                # Save in the data-store
                new_blogpost.put()

            self.redirect("/blog")
        else:
            self.redirect("/login")

    def get(self):
        blogpost_query = Blogpost.query(ancestor=App.DEFAULT_KEY).order(-Blogpost.date)
        blogposts = blogpost_query.fetch()

        result = []
        for blogpost in blogposts:
            result.append({"title": blogpost.title, "bpost": blogpost.bpost, "photoKey": blogpost.photo_key})

        self.response.write(json.dumps({"titles": result}))