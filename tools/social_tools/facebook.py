import socket
import requests
from tools.social_tools.reqtor import TorRequest
import argparse
import requests
import pyquery


def facebook(user, pw, pas):
    def login(session, email, password):
        
        '''
        Attempt to login to Facebook. Returns user ID, xs token and
        fb_dtsg token. All 3 are required to make requests to
        Facebook endpoints as a logged in user. Returns False if
        login failed.
        '''

        # Navigate to Facebook's homepage to load Facebook's cookies.
        response = session.get('https://m.facebook.com')
        
        # Attempt to login to Facebook
        response = session.post('https://m.facebook.com/login.php', data={
            'email': email,
            'pass': password
        }, allow_redirects=False)
        
        # If c_user cookie is present, login was successful
        r = str(response.cookies)
        if 'checkpoint=' in r:

            return True
        else:
            return False 
    print("[FACE] connecting requests to tor...")
    session=TorRequest(password=pas)
    session.reset_identity()

#    session.headers.update({
#        'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
#    })

    user_id= login(session, user, pw)
    print(user_id)
    if user_id:
        return True
    else:
        return False