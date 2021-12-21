#!/usr/bin/python3

import requests
import json
import sys

# get arguments from onboard script and pass them to variables
userID = str(sys.argv[1])
serial_number = str(sys.argv[2])


def checkOutDevice():
    #JSON template from mosyle to create a user
    payload ='''
    {
        "accessToken": "c8a5d56d90a0a21d10218906cd4424a52dcc54a154c1c826958255188d5421ad",
        "elements": [
            {
                "operation": "assign_device",
                "id": "new.user.1",
                "serial_number": "AAAAAAAAAAAA"
            }
        ]
    }
    '''
    # Converts the raw JSON to a python object so we can work with it
    dataToSend = json.loads(payload)

    #for loop to cycle through the newly created python object so we can find and replace
    #the exact values
    #replaces the template data with the passed in arguements
    # for person in dataToSend['elements']:
    #         person['id'] = userID
    #         person['serial_number'] = serial_number
            
            
    #puts the object into a big string
    # finishedData = json.dumps(dataToSend)

    # sends a post request to mosyle API with the modified template finishedData string as the payload        
    r = requests.post('https://managerapi.mosyle.com/v2/users', data=payload)
    #prints the JSON that comes back from the API
    #If "status":"OK" then user was created successfully
    print(r.text)

checkOutDevice()
