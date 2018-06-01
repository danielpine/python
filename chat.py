# -*- coding: utf-8 -*-
import requests
import itchat

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
KEY = '1107d5601866433dba9599fac1bc0083'
KEY = '71f28bf79c820df10d39b4074345ef8c'
KEY = 'eb720a8970964f3f855d863d24406576'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

itchat.auto_login(hotReload=True)
itchat.run()
