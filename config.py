import itchatmp

TOKEN='testitchatmp'
APPID= 'wx39472499ed448bf2'
APPSECRET='86157bec4e5e28e46f251690786ca08b'

def update_config():
    itchatmp.update_config(itchatmp.WechatConfig(
    token=TOKEN,
    appId = APPID,
    appSecret = APPSECRET))
