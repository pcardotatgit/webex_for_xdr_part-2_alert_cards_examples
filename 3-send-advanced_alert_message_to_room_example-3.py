'''
    Based on example 2 this alert message is another static example ( see cards_content variable bellow ).
    The alert message contain Targeted systems and Suspicious Observables. These object are displayed thru 2 separate lists.
    Objects to isolate or to block can be selected separately.
    The list are hidden by default and they can be displayed thanks to button
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
                }                   
            ],
            "actions": [
                {
                    "type": "Action.ShowCard",
                    "title": "Targeted Systems",
                    "card": {
                        "type": "AdaptiveCard",
                        "body": [
                            {
                                "type": "TextBlock",
                                "text": "Select Systems to isolate",
                                "color": "Warning",
                                "size": "Medium",
                                "wrap": True
                            },
                            {
                                "type": "Input.ChoiceSet",
                                "id": "systems",
                                "style": "expanded",
                                "isMultiSelect": True,
                                "choices": [
                                    {
                                        "title": "10.10.10.10",
                                        "value": "10.10.10.10"
                                    },                                    
                                    {
                                        "title": "20.20.20.20",
                                        "value": "20.20.20.20"
                                    }
                                ]
                            }
                        ],
                        "actions": [
                            {
                                "type": "Action.Submit",
                                "title": "Isolate Selected Systems",
                                "data": {
                                    "systems_to_isolate": "Targeted Systems"
                                }
                            }
                        ],
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
                    }
                },
                {
                    "type": "Action.ShowCard",
                    "title": "Suspicious observables",
                    "card": {
                        "type": "AdaptiveCard",
                        "body": [
                            {
                                "type": "TextBlock",
                                "text": "Suspicious Observables :",
                                "color": "Warning",
                                "size": "Medium",
                                "wrap": True
                            },
                            {
                                "type": "Input.ChoiceSet",
                                "id": "observables",
                                "style": "expanded",
                                "isMultiSelect": True,
                                "choices": [
                                    {
                                        "title": "192.168.100.45",
                                        "value": "192.168.100.45"
                                    },                                    
                                    {
                                        "title": "192.168.100.100",
                                        "value": "192.168.100.100"
                                    },                                    
                                    {
                                        "title": "200.200.200.200",
                                        "value": "200.200.200.200"
                                    }
                                ]
                            }
                        ],
                        "actions": [
                            {
                                "type": "Action.Submit",
                                "title": "Block Selected Objects",
                                "horizontalAlignment": "Center",
                                "data": {
                                    "objects_to_block": "Suspicious observables"
                                }
                            }
                        ],
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
                    }
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
    "markdown": "!  XDR ALERT !",
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