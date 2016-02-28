from base_handler import Handler

class MainHandler(Handler):
    def get(self):
        self.render("writersblock.html")
