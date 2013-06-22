from weibo import *

APP_KEY = '204574897' # app key
APP_SECRET = '16090a4faf9ffdf06c9d377f26f4abd7' # app secret
CALLBACK_URL = 'www.renren.com/yuanpuhao' # callback url

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)

access_token = "2.00JjFaTB0HR4qN6e7fe0fda00zhShF"
expires_in = "1529485386"

client.set_access_token(access_token, expires_in)
print client.statuses.user_timeline.get()
print client.statuses.update.post(status=u"Puhao Yuan the stupid guy is doing stupid thing!")