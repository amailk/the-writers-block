import requests
import json

from base_handler import Handler
from app import App

class CallbackHandler(Handler):
    def get(self):
        code = self.request.get('code')

        json_header = {'content-type': 'application/json'}

        token_url = "https://the-writers-block.auth0.com/oauth/token"

        token_payload = {
            'client_id':     '5UMLa74caWbeFlfTswRlwxeM2Si4nVYN',
            'client_secret': 'JvN5U-WTAfHEANd4bKbWRGgSFT_vqGDSd1YMSAnPXaO7xinKklnzx09546Crl9RO',
            'redirect_uri':  'http://127.0.0.1:8080/callback',
            #'redirect_uri':  'http://port-key.appspot.com/callback',
            'code':          code,
            'grant_type':    'authorization_code'
        }

        token_info = requests.post(token_url, data=json.dumps(token_payload), headers=json_header).json()

        print "Token Info", token_info

        user_url = "https://{domain}/userinfo?access_token={access_token}" \
              .format(domain='the-writers-block.auth0.com', access_token=token_info['access_token'])

        user_info = requests.get(user_url).json()


        # We're saving all user information into the session
        App.session['profile'] = user_info

        # Redirect to the User logged in page that you want here
        # In our case it's /dashboard
        print "Callback succeeded"
        self.redirect('/')