#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

from handlers.page_handler import PageHandler
from handlers.login_handler import LoginHandler, LogoutHandler
from handlers.blogpost_handler import BlogpostHandler
from handlers.image_handler import ImageHandler
from handlers.profile_handler import ProfileHandler
from handlers.main_handler import MainHandler
from handlers.page_handler import PageHandler

app = webapp2.WSGIApplication([
    ('/profile', ProfileHandler),
    ('/logout', LogoutHandler),
    ('/login', LoginHandler),
    ('/blogpost', BlogpostHandler),
    ('/blog', PageHandler),
    ('/images', ImageHandler),
    ('/', MainHandler)
], debug=True)