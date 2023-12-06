'''
    static example 1 of alert message send to webex room. the card contains object selection
    static card is contained intot the cards_content variable
'''
import requests
import sys
import config  as conf
from crayons import *

ROOM_ID=conf.DESTINATION_ROOM_ID
ACCESS_TOKEN=conf.BOT_ACCESS_TOKEN
version=conf.version

URL = 'https://webexapis.com/v1/messages'
alert_message="Suspicious Activity Detected"

attachment={
    "roomId": ROOM_ID,
    "markdown": "Infection Alert !",
    "attachments": [
        {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {    
                "type": "AdaptiveCard",
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "version": "1.2",
                "id": "title",
                "body": [
                    {
                        "type": "TextBlock",
                        "text": "! XDR ALERT !",
                        "size": "Large",
                        "color": "Warning",
                        "horizontalAlignment": "Center"
                    },
                    {
                        "type": "Container",
                        "items": [
                            {
                                "type": "TextBlock",
                                "text": alert_message,
                                "wrap": True,
                                "color": "Attention"
                            }
                        ]
                    },  
                    {
                        "type": "TextBlock",
                        "color": "Accent",                        
                        "text": "Targeted Endpoints :"
                    },                    
                    {
                        "type": "TextBlock",
                        "color": "Light",                        
                        "text": "10.10.10.7 - endpoint"
                    },                      
                    {
                        "type": "TextBlock",
                        "text": "Suspicious Objects",
                        "size": "Medium",
                        "color": "Warning",
                        "horizontalAlignment": "Center"                        
                    },                     
                    {
                        "type": "Input.Toggle",
                        "title": "13.15.48.58",
                        "id": "aa",
                        "value": "13.15.48.58"
                    },
                    {
                        "type": "Input.Toggle",
                        "title": "192.168.158.26",
                        "id": "ab",
                        "value": "192.168.158.26"
                    }                    
                ],
                "actions": [
                    {
                        "type": "Action.Submit",
                        "title": "Block IPs in Firewalls"                                                
                    }
                ]                
            }
        }
    ]
}

headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,
           'Content-type': 'application/json;charset=utf-8'}
#post_data = {'roomId': ROOM_ID,'text': MESSAGE_TEXT}
#post_data = {'roomId': ROOM_ID,'attachments': attachment3}
response = requests.post(URL, json=attachment,headers=headers)
if response.status_code == 200:
    # Great your message was posted!
    #message_id = response.json['id']
    #message_text = response.json['text']
    print("New message created")
    #print(message_text)
    print("====================")
    print(response)
else:
    # Oops something went wrong...  Better do something about it.
    print(response.status_code, response.text)