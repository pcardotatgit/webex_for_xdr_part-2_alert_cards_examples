# Webex Card for XDR alerts

These scripts give examples of Alert Adaptative Cards for Security Alert. 

The idea here is to make the message efficient for the Security Operator who will receive it. Make him able to understand in one view the situation and make instant decisions

To acheive this the header of the message will contain a very short description of the security issue. 
Second the next part will be a list of the targeted machines within the organisations that are targeted by tha Attack. With check boxes for each of them that allow to select them and trigger an isolation action.

The third part of the message will be the list of malicious observables which are the source of the attack, with check boxes for each of them that allow to select them and to trigger a blocking action.

In order to make readers able to understand how to built advanced webex cards, we share several python scripts which start with a basic static card examples and ends with an advanced one which is dynamically created.

In the 3 first scripts, the Cards JSON data are statics. This give you examples of working JSON data

In **4-send-advanced_dynamic_alert_message_to_room_example.py** example, the target and observables list are dynamically builted from text files located into the **./targets_and_observables** directory.

The final goal is to finalize python functions that create the Webex cards JSON data from 2 list inputs. The first one is the target list and the second one is the observable list.

Then depending on the target and observable sources, the work to do will be to create dedicated collecting and parsing functions.

# Installation

## Step 0. Prerequisit

You must have created a webex bot first. If your bot is located into your laptop then use **ngork** to make it available on the INTERNET.

Have a look to the instructions here for that [Create a webex bot](https://github.com/pcardotatgit/Create_a_Webex_bot_for_XDR_Alerts)

## Step 1. Create a working directory

Create a working directory into your laptop. Open a terminal CMD window into it. Name It XDR_BOT for example.

## Step 2. Copy the code into your laptop

The Download ZIP Method

The easiest way for anyone not familiar with git is to copy the ZIP package available for you in this page. Click on the Code button on the top right of this page. And then click on Download ZIP.

Unzip the zip file into your working directory.

The "git clone" method with git client

And here under for those of you who are familiar with Github.

You must have a git client installed into your laptop. Then you can type the following command from a terminal console opened into your working directory.

    git clone https://github.com/pcardotatgit/webex_for_xdr_part-2_alert_cards_examples.git

## Step 3. Go to the code subfolder

Once the code unzipped into your laptop, then Go to the code subfolder.

## Step 4. Create a Python virtual environment

It is still a best practice to create a python virtual environment. Thank to this you will create a dedicated package with requested modules for this application.

### Create a virtual environment on Windows

    python -m venv venv 

### Create a virtual environment on Linux or Mac

    python3 -m venv venv

Depending on the python version you installed into your Mac you might have to type either 

- python -m venv venv

or maybe

- python3 -m venv venv    : python3 for python version 3.x  

or maybe 

- python3.9 -m venv venv  : if you use the 3.9 python version

And then move to the next step : Activate the virtual environment.

### Activate the virtual environment on Windows

    venv\Scripts\activate

### Activate the virtual environment on Linux or Mac

    source venv/bin/activate    

## Step 5. Install needed python modules

You can install them with the following 2 commands one after the other ( Windows / Mac / Linux ):

The following command might be required if your python version is old.

    python -m pip install --upgrade pip   

Then install required python modules ( Windows / Mac / Linux )

    pip install -r requirements.txt

## Configuration and prerequisit

1- You must have a valid **BOT_ACCESS_TOKEN**. That means that you must have created a Webex BOT first.
2- You must know the **room_id** of the destination webex room and the Webex Bot must be invited into it.

Then Edit the **config.py** file and set the correct values for the **DESTINATION_ROOM_ID** and **BOT_ACCESS_TOKEN**

## Run the script

Just run the script 

    python select_and_send_an_advanced_webex_card.py
    
The expected result is to see the Alert Card to be displayed into the webex room
    
## Where to go Next ? : Built the Webex Bot Logic

Go to the next chapter in order to learn about how to built the Webex Bot Logic

[webex_for_xdr_part-3_webhook_bot](https://github.com/pcardotatgit/webex_for_xdr_part-3_webhook_bot)

Go to the previous chapter 

[webex_for_xdr_part-1_card_examples](https://github.com/pcardotatgit/webex_for_xdr_part-1_card_examples)