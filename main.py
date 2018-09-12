import itchatmp
import itchatmp.content
import config

config.update_config()

@itchatmp.msg_register(itchatmp.content.TEXT)
def text_reply(msg):
    print(msg)
    if msg['Content']=='g':
        print('gggg'*20)
        r = itchatmp.users.get_user_info(msg['FromUserName'])
        print(r)
    return 'I received: ' + msg['Content']

@itchatmp.msg_register(itchatmp.content.EVENT)
def event_come(msg):
    if msg['Event']=='LOCATION':
        print("@@" * 20)
        print(msg['Longitude'],msg['Latitude'],msg['Precision'])



##@itchatmp.msg_register(itchatmp.content.INCOME_MSG)
def text_reply(msg):
    print('='*20)
    print(msg)
    print('******'*20)



itchatmp.run()
