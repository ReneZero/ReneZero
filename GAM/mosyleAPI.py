#!/usr/bin/python3

import requests
import json
import sys

# get arguments from onboard script and pass them to variables
newID = str(sys.argv[1])
newUserEmail = str(sys.argv[1])
schoolSite = str(sys.argv[2])
teacherOrStaff = str(sys.argv[3])
newUserName = str(sys.argv[4]) + " " + str(sys.argv[5])

#JSON template from mosyle to create a user
payload = '''
{
    "accessToken": "PASTE API KEY HERE",
    "elements": [
    {
        "id": "aaa",
        "operation": "save",
        "name": "User Staff Test",
        "type": "STAFF",
        "welcome_email": 0,
        "email": "ReneAPItestv2@renizzle818.com",

        "locations": [
            {
                "name": "BCCS"
            }
        ]
    }
    ]
}
'''
# Converts the raw JSON to a python object so we can work with it
dataToSend = json.loads(payload)

#for loop to cycle through the newly created python object so we can find and replace
#the exact values
#replaces the template data with the passed in arguements
for person in dataToSend['elements']:
        person['id'] = newID
        person['locations'] = [{'name': schoolSite}]
        person['type'] = teacherOrStaff
        person['email'] = newUserEmail
        person['name'] = newUserName
        
        
#puts the object into a big string
finishedData = json.dumps(dataToSend)

# sends a post request to mosyle API with the modified template finishedData string as the payload        
r = requests.post('https://managerapi.mosyle.com/v2/users', data=finishedData)
#prints the JSON that comes back from the API
#If "status":"OK" then user was created successfully
print(r.text)
