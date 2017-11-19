from urllib import request, parse
import json

class Wechat_Notifications:

    def __init__(self, text, key):
        self.title = text
        self.message = ''
        self.key = key
        pass

    def push(self, text):
        self.message += text + "\n\n"

    def post(self):
        url = 'https://sc.ftqq.com/' + self.key + '.send'
        parms = {
           'text' : self.title,
           'desp' : self.message
        }
        querystring = parse.urlencode(parms)
        u = request.urlopen(url+'?' + querystring)
        resp = json.loads(u.read().decode())
        # errno = resp['errno']
        errmsg = resp['errmsg']
        return errmsg



# wn = Wechat_Notifications("Hello, World!")
# # 粗体 #
# wn.push("**This is just a test**")
# # 无序标记 #
# wn.push("* Now testing...")
# # 粗体 #
# wn.push("__This is just a test__")
# # 引用 #
# wn.push("> Now testing...")
# print(wn.post())