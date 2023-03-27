#!flask/bin/python

import requests
from flask import Flask
from flask import request
from config import validator, devices, access_points, secret

# Variables to use with telegram
from config import telegram_chatid, telegram_token, enable_telegram
# Variables to use with webex
from config import webex_chatid, webex_token, enable_webex


def location_analytics(data):

    for u in devices:
        for i in data['data']['observations']:
            if i['clientMac'] == u['MAC']:
                u['location_new'] = i['location']
                if u['initialiser'] == 0:
                    u['location'] = u['location_new']
                    u['initialiser'] = 1
                    u['location_ap'] = access_points[str(data['data']['apMac'])]
                else:
                    print('Sensor: ' + u['MAC_alias'])
                    location_x = round(u['location']['x'][0])
                    location_y = round(u['location']['y'][0])
                    location_new_x = round(u['location_new']['x'][0])
                    location_new_y = round(u['location_new']['y'][0])

                    if location_x == location_new_x and location_y == location_new_y:
                        print('The Sensor ' + u['MAC_alias'] + 'did not move')
                    else:
                        print('The Sensor: ' + u['MAC_alias'] + ' moved')
                        if enable_telegram:
                            telegram_bot_sendtext('The Bluetooth Device: ' + u['MAC_alias'] + ' Moved! Current Position: ' \
                                                + str(u['location_new']) + '    AP of origin was: *'  + u['location_ap'] + \
                                                    '*    Current AP: *' + access_points[str(data['data']['apMac'])])
                        if enable_webex:
                            webex_sendmessage('The Bluetooth Device: *' + u['MAC_alias'] + '* Moved! Current Position: ' \
                                                + str(u['location_new']) + '    AP of origin was: *'  + u['location_ap'] + \
                                                    '*    Current AP: *' + access_points[str(data['data']['apMac'])] + '*')
                        u['location'] = u['location_new']
                        u['location_ap'] = access_points[str(data['data']['apMac'])]



def telegram_bot_sendtext(bot_message):
    
    send_text = 'https://api.telegram.org/bot' + telegram_token + '/sendMessage?chat_id=' + telegram_chatid + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response.json()


def webex_sendmessage(bot_message):
    apiUrl = 'https://webexapis.com/v1/messages'
    httpHeaders = { 'Content-type': 'application/json', 'Authorization': 'Bearer ' + webex_token }

    body = { 'roomId': webex_chatid, 'text': bot_message }

    response = requests.post( url = apiUrl, json = body, headers = httpHeaders )
    return response.json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def send_validator():
    print("validator sent to: ", request.environ['REMOTE_ADDR'])
    return validator


@app.route('/', methods=['POST'])
def receive_data():
    if not request.json or not 'data' in request.json:
        return("Invalid data", 402)
    
    data = request.json

    print("Received POST from ", request.environ['REMOTE_ADDR'])


    if data['secret'] != secret:
        print("secret invalid:", data['secret'])
        return("invalid secret", 403)
    else:
        print("secret verified: ", data['secret'])

    location_analytics(data)

    return "Location Received"

if __name__ == '__main__':
    app.run(debug=False)