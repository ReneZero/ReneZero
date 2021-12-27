#!/usr/bin/python3

import requests
import json
import sys

# get arguments from onboard script and pass them to variables
userID = str(sys.argv[1])
uniqueID = "0"
didYouFindIt = False
counter = 2
payload ='''
{
    "accessToken": "PASTE API KEY HERE",
    "options": {
        "os": "mac",
        "page": "1",
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
"accessToken": "PASTE API KEY HERE",
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
editPayload = json.loads(payload)
def checkInMacOS():
    global didYouFindIt
    global counter
    global uniqueID
    #JSON template from mosyle to create a user
        
    #### Getting list of devices
    r = requests.post('https://managerapi.mosyle.com/v2/listdevices', data=payload)
    json_data = json.loads(r.text)
    print("Finding Device...")
    ####Filtering until we find the one tied to their email
    for device in json_data['response']['devices']:
        if 'userid' in device:
            if device['userid'] == userID:
                ####grabbing deviceUDID
                uniqueID = device['deviceudid']
                didYouFindIt = True
            else:
                while didYouFindIt is False:
                        pageUp(str(counter))
                        counter = counter + 1
                                
    
    # Converts the raw JSON template to a python object so we can work with it
    dataToSend = json.loads(payload2)
    #########Replacing UDID with the one we grabbed
    for device2 in dataToSend['elements']:
        device2['devices'] = [uniqueID]        
    #puts the object into a big string
    finishedData = json.dumps(dataToSend)
    ##########sending API Request in order to change the device to limbo using the UDID
    print("Changing device to limbo...")
    r2 = requests.post('https://managerapi.mosyle.com/v2/bulkops', data=finishedData)
    print(r2.text)
    #######################################################################

def pageUp(pageNum):
    global didYouFindIt
    global uniqueID
    editPayload['options']['page'] = str(pageNum)
    print("Finding Device...")
    pageUpRequest = json.dumps(editPayload)
    r3 = requests.post('https://managerapi.mosyle.com/v2/listdevices', data=pageUpRequest)
    r3Response = json.loads(r3.text)
    for device in r3Response['response']['devices']:
        if 'userid' in device:
            if device['userid'] == userID:
            ####grabbing deviceUDID
                uniqueID = device['deviceudid']
                didYouFindIt = True
checkInMacOS()
