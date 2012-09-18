import re
import requests
import time
import sys

form_action_re = re.compile(r'name="weblogin_form" method="POST" action="([^"]+)"')
form_password_re = re.compile(r'name="password" value="([^"]+)"')

if __name__ == '__main__':
    user = sys.argv[1]
    action = 'http://10.0.4.13/ING_Cafe.php'
    while True:
        print 'signing in'
        resp = requests.post(action, {'user': user})

        action_match = form_action_re.search(resp.text)
        pw_match = form_password_re.search(resp.text)

        if action_match and pw_match:
            action = action_match.group(1)
            pw = pw_match.group(1)

            requests.post(action, {'user': user, 'password': pw, 'cmd': 'authenticate', 'Login': '"Log In"'})
            print 'signed in'
        else:
            print 'already signed in'

        time.sleep(30)
