from weibo import *

APP_KEY = '204574897' # app key
APP_SECRET = '16090a4faf9ffdf06c9d377f26f4abd7' # app secret
CALLBACK_URL = 'www.renren.com/yuanpuhao' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)


#access_token = "2.00ufE2sD0HR4qNe6cf275dacOn_iEB"
#expires_in = "1372014057"

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
print url

code_get = raw_input("print code:")
print code_get
code = code_get
r = client.request_access_token(code)
access_token = r.access_token
expires_in = r.expires_in

client.set_access_token(access_token, expires_in)
#print client.statuses.user_timeline.get()
print client.statuses.update.post(status=u"Stupid guy is doing stupid thing!")
