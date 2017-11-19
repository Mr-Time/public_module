from Wechat_Notifications import *

wechat_test = Wechat_Notifications('Message','SCU16257T52960940d333f404fb12005f47b1d8875a11791dd5bc3')
wechat_test.push('**This is the title.**')
wechat_test.push('This is the first line.')
wechat_test.post()