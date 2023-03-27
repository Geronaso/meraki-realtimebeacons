# Meraki variables
validator = 'The validator localized at the meraki location and scanning page'
secret = 'An Secret to use in the application and the meraki scanning API'

# Telegram Variables, change to True/False if you want it enabled
enable_telegram = False
telegram_chatid = 'The chatId of the Telegram chat that your bot'
telegram_token = 'The token of your Telegram bot'

# Webex Variables, change to True/False if you want it enabled
enable_webex = True
webex_chatid = 'The chat ID of the Webex chat, this ID can be retrieved by copying the chat link webexteams://im?space=the-value-here-is-the-chatid'
webex_token = 'Your webex token, can be accessed on the Webex API page'



# Edit the MAC
devices = [
    {
    'MAC': 'The MAC address of the device you want to track',
    'MAC_alias': 'A name to be used for this device',
    'location': '',
    'location_new': '',
    'location_ap': '',
    'initialiser': 0
    },
    {
    'MAC': '18:fe:34:d7:ff:aa',
    'MAC_alias': 'Sensor 1',
    'location': '',
    'location_new': '',
    'location_ap': '',
    'initialiser': 0
    }
]

access_points = {
    'The MAC address of your access point': 'A name for the access point',
    '18:fe:34:d7:ff:aa': 'Access Point 1'
}