'''
#Setup the script to text me when I receive a new skype message
#If you need to see how many active windows there currently are
test = pyautogui.getAllTitles()
active_windows = [x for x in test if x != '']
print(len(active_windows))

'''

import time
import pyautogui
from twilio.rest import Client

count = 0
while count < 1:
    test = pyautogui.getAllTitles()
    active_windows = [x for x in test if x != '']
    if len(active_windows) > 10:
        account_sid = '*******************'
        auth_token = '******************'
        client = Client(account_sid, auth_token) 
        message = client.messages.create( 
                                  body='Work', 
                                  from_='*****', 
                                  to='******'
                              )
        print(message.sid)
        count += 1