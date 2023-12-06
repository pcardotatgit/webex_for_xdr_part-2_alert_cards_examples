'''
    Static example 2 of an alert message with object selection, sent to webex room.
    This example is based on example 1 but with nicer look andd feel
    static card is contained intot the cards_content variable
'''
import requests
import sys, os
import config  as conf
from crayons import *
import json

ROOM_ID=conf.DESTINATION_ROOM_ID
ACCESS_TOKEN=conf.BOT_ACCESS_TOKEN
version=conf.version
URL = 'https://webexapis.com/v1/messages'
alert_message="Suspicious Activity Detected"
cards_content=[
    {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {    
            "type": "AdaptiveCard",
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.3",
            "backgroundImage": {
                "url": "https://i.postimg.cc/vBxnRp06/sky2.jpg",
                "verticalAlignment": "Center"
            },             
            "id": "title",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "! XDR ALERT !",
                    "color": "Attention",
                    "weight": "Bolder",
                    "size": "ExtraLarge",                        
                    "horizontalAlignment": "Center"
                },
                {
                    "type": "Container",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": alert_message,
                            "wrap": True,
                            "color": "Attention",
                            "horizontalAlignment": "Center"
                        }
                    ]
                },
                {
                    "type": "Container",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Targeted Systems",
                            "size": "Medium",
                            "color": "Warning",
                            "horizontalAlignment": "Center"      
                        },
                        {
                            "type": "Input.Toggle",
                            "title": "10.10.10.7",
                            "id": "aa",
                            "value": "10.10.10.7"
                        }, 
                        {
                            "type": "Input.Toggle",
                            "title": "10.10.10.10",
                            "id": "ab",
                            "value": "10.10.10.10"
                        }                      
                    ]                        
                },
                {
                    "type": "ActionSet",
                    "actions": [
                        {
                            "type": "Action.Submit",
                            "title": "Isolate Targeted Systems",
                            "Style":"destructive",
                        }
                    ],
                    "horizontalAlignment": "Center"
                }                    
            ]
        }
    }
]  

def load_card_and_send_it(cards_content):
    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,
               'Content-type': 'application/json;charset=utf-8'}
    print(red(cards_content))
    attachment={
    "roomId": ROOM_ID,
    "markdown": "! XDR ALERT !",
    "attachments": cards_content
    }
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
    
if __name__=="__main__":
    load_card_and_send_it(cards_content)