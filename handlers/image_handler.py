from base_handler import Handler
from app import App
from models.blogpost import Blogpost

class ImageHandler(Handler):
    def get(self):
        photo_key = self.request.get("photo_key")
        query = Blogpost.query(Blogpost.photo_key == photo_key, ancestor=App.DEFAULT_KEY)
        blogposts = query.fetch()
        blogpost = blogposts[0]

        if blogpost.photo:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(blogpost.photo)
        else:
            self.response.out.write('No Image')