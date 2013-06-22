from weibo import *

APP_KEY = '204574897' # app key
APP_SECRET = '16090a4faf9ffdf06c9d377f26f4abd7' # app secret
CALLBACK_URL = 'www.renren.com/yuanpuhao' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print url

code_get = raw_input("print code:")
print code_get
code = code_get
r = client.request_access_token(code)
access_token = r.access_token
expires_in = r.expires_in 
print access_token
print expires_in