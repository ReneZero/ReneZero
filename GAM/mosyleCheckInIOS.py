#!/usr/bin/python3

import requests
import json
import sys

# get arguments from onboard script and pass them to variables
userID = str(sys.argv[1])
uniqueID = "0"

def checkInIOS():
    #JSON template from mosyle to create a user
    payload ='''
    {
        "accessToken": "c8a5d56d90a0a21d10218906cd4424a52dcc54a154c1c826958255188d5421ad",
        "options": {
            "os": "ios",
            "specific_columns": [
                "userid",
                "serial_number",
                "deviceudid"
            ]
        }
    }
    '''
    payload2 = '''
    {
    "accessToken": "c8a5d56d90a0a21d10218906cd4424a52dcc54a154c1c826958255188d5421ad",
    "elements": [
        {
            "operation": "change_to_limbo",
            "devices": [
                "00008027-000C45693A6A402E"
                ]
            }
        ]
    }
    '''
    #### Getting list of devices
    r = requests.post('https://managerapi.mosyle.com/v2/listdevices', data=payload)
    json_data = json.loads(r.text)
    ####Filtering until we find the one tied to their email
    for device in json_data['response']['devices']:
        if 'userid' in device:
            if device['userid'] == userID:
                ####grabbing deviceUDID
                uniqueID = device['deviceudid']
    
    # Converts the raw JSON to a python object so we can work with it
    dataToSend = json.loads(payload2)
    #########Replacing UDID with the one we grabbed
    for device2 in dataToSend['elements']:
        device2['devices'] = [uniqueID]        
    #puts the object into a big string
    finishedData = json.dumps(dataToSend)
    ##########sending API Request in order to change the device to limbo using the UDID
    r2 = requests.post('https://managerapi.mosyle.com/v2/bulkops', data=finishedData)
    print(r2.text)
    #######################################################################
    
checkInIOS()
