# realtime-beacons
Easily start receiving notifications in real time if your bluetooth devices connected to Meraki move with realtime-beacons.

This program is a simple web server that receives data from Cisco Meraki Scanning API. It then process the JSON data and send a message in real time through Telegram or Webex APIs if a bluetooth device has moved.

+ It uses Flask as the Web Service Application
+ It supports Webex and Telegram APIs to post chat messages

## Requirements
Flask >= 2.2.3
Python >= 3.9

# Quickstart


```
git clone <<this repo>>
cd 
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
export API_KEY='DEV'
flask --app realtime-beacons --debug run
```


## Add your devices

Edit the config.py file variables.

```
validator = 'The validator localized at the meraki location and scanning page'
secret = 'An Secret to use in the application and the meraki scanning API'
```
> **_NOTE:_**  These are Meraki related variables, you should edit with your information.

```
enable_telegram = False
telegram_chatid = 'The chatId of the Telegram chat that your bot'
telegram_token = 'The token of your Telegram bot'
```
> **_NOTE:_**  These are the Telegram variables, enable by changing the value to True. For more help on how to get. For more help on how to get these information you can read its documentation: https://core.telegram.org/bots/api


```
enable_webex = True
webex_chatid = 'The chat ID of the Webex chat, this ID can be retrieved by copying the chat link webexteams://im?space=the-value-here-is-the-chatid'
webex_token = 'Your webex token, can be accessed on the Webex API page'
```
> **_NOTE:_**  Webex related variables, enable by changing the value to True. For more help on how to get. For more help on how to get these information you can read its documentation: https://developer.webex.com/docs/getting-started


```
devices = [
    {
    'MAC': 'The MAC address of the device you want to track',
    'MAC_alias': 'A name to be used for this device',
    ...
```
> **_NOTE:_**  These are the two values you should edit on this list, by adding your device MAC address and a name to it. You can add more devices at will by adding more entries to the list of dictionaries.


```
access_points = {
    'The MAC address of your access point': 'A name for the access point',
    '': ''
}
```
> **_NOTE:_** Edit this dictionary and add your access points address and names.


## Enabling Scanning API on Meraki

Here you can find more help on enabling the Scanning API on Meraki.

https://developer.cisco.com/meraki/scanning-api/#!enable-scanning-api/enable-location-api

## Serving the Web Service

The server that runs this application must have internet access to receive the post from Meraki. Some ways to do this include Ngrok or 
Cloud providers.

Through Ngrok you can do the following steps to serve on a Debian based system

```
sudo apt-get install ngrok
ngrok http 5000
```

Then use the https link provided through Ngrok. This will result in a reverse proxy to our application.

## Considerations

This should not be used on production environments, these steps are for developing and testing environments.


# Evaluation

You will start receiving messages at yout webex/telegram chat if a device move at real time:


![alt text](https://github.com/Geronaso/meraki-realtimebeacons/blob/main/images/result.png?raw=true)

## Author

### Written by Cézar Murilo (2022) and Developed by NAPIT

https://www.napit.com.br/



