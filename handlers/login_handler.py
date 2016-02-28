from base_handler import Handler
from app import App


class LoginHandler(Handler):
    def get(self):
        self.render("login.html")

class LogoutHandler(Handler):
    def get(self):
        App.session['profile'] = None
        self.redirect('/')