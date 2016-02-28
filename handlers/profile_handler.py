import uuid
import json

from base_handler import Handler
from app import App
from models.profile import Profile

class ProfileHandler(Handler):

    def post(self):
        photo = str(self.request("photo"))
        user_name = self.request("user_name")
        first_name = self.request("first_name")
        last_name = self.request("last_name")
        twitter = self.requst("twitter")

        user= App.session.get('profile')

        if user:
            invalidFieldFlag = False
            if len(user_name.strip()) == 0:
                ProfileHandler.invalidUser_Name = True
                invalidFieldFlag = True
            if len(first_name.strip()) == 0:
                ProfileHandler.invalidFirst_Name = True
            if len(last_name.strip()) == 0:
                ProfileHandler.invalidLast_Name = True
            if not invalidFieldFlag:
                ProfileHandler.invalidUser_Name = ProfileHandler.invalidFirst_Name = ProfileHandler.invalidLast_Name = False

                user_id = user['user_id']
                new_profile = Profile(parent=App.DEFAULT_KEY)
                new_profile.user_name = user_name
                new_profile.first_name = first_name
                new_profile.last_name = last_name
                new_profile.photo = photo
                new_profile.photo_key = uuid.uuid4().hex
                new_profile.user_id = user_id


                new_profile.put()
            self.redirect("/#profiles")
        else:
            self.redirect("#login")

    def get(self):
        user = App.session.get('profile')
        print "User", user

        if user:
            user_id = user['user_id']
            self.render("profile.html")
        else:
            self.redirect("/login")