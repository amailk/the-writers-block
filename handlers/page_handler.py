from base_handler import Handler
from app import App
from models.blogpost import Blogpost

class PageHandler(Handler):
    # Status for the most recently added diary entry to be valid or invalid
    invalidTitle = False
    invalidPost = False
    invalidPhoto = False

    def get(self):
        user = App.session.get('profile')
        print "User", user

        #if user:
            #Get all the blogpost entries, sorted by date
        user_id = "user_id" #user['user_id']
        blogpost_query = Blogpost.query(Blogpost.user_id == user_id, ancestor=App.DEFAULT_KEY).order(-Blogpost.date)
        blogposts = blogpost_query.fetch()
        for blogpost in blogposts:
            blogpost.date_text = blogpost.date.strftime('%Y, %b %d')
        print blogposts
        self.render("blogpage.html", blogposts=blogposts, invalidTitle=PageHandler.invalidTitle, invalidPost=PageHandler.invalidPost, invalidPhoto=PageHandler.invalidPhoto, logout_url='/logout')
        #else:
        #    self.redirect("/login")