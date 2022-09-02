import os
import termux_api
import time
import sms
from pysondb import getDb

received_sms = getDb('sms.json')
ringtone = 'ringtone.mp3'
api = termux_api
count = 0

def findme():
    api.media_player_play_file(ringtone)
    api.volume_set('music', 100)
    while count < 10:
        for i in range(0, 20):
            api.vibrate(1000, True)
            api.torch(True)
            time.sleep(0.5)
            api.torch(False)

while True:
    time.sleep(5)
    messages = sms.readSMS()
    for message in messages:
        data = {
            'body': message['body'],
            'message_id': message['_id'],
            'type': message['type']
        }
        if len(received_sms.getByQuery(data)) > 0:
            continue
        else:
            body = message['body'].split(' ')
            if body[0] == 'FINDME' and message['type'] == 'inbox':
                received_sms.add(data)
                findme()
            if body[0] == 'MISSING' and message['type'] == 'inbox':
                os.system('')
            else:
                received_sms.add(data)