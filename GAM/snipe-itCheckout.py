import requests
import sys
import json

userEmail = str(sys.argv[1])
userID = "0"
assetTag = str(sys.argv[2])
assetID = "0"

def getAssetID():
    global assetID
    url = "https://inventory.ypics.org/api/v1/hardware/bytag/" + assetTag

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer Replace API key Here"
    }

    response = requests.request("GET", url, headers=headers)

    json_data = json.loads(response.text)

    assetID = json_data['id']
    

def getUserID():
    global userID
    #####Get user ID by looking up email
    url = "https://inventory.ypics.org/api/v1/users?limit=1&offset=0&sort=created_at&order=desc&username=" + userEmail + "&deleted=false&all=false="

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer Replace API key Here"
    }

    response = requests.request("GET", url, headers=headers)

    json_data = json.loads(response.text)
## grab user data info from the list rows into a string 
    userID = json_data['rows'][0]['id']
        

def checkOutAsset():
    global assetID
    global userID
    ######Check out using asset Id and User ID
    ### input asset ID
    url = "https://inventory.ypics.org/api/v1/hardware/" + str(assetID) + "/checkout"

    payload = {
        ###input userID we found as the value of the assigned user key
        "checkout_to_type": "user",
        "assigned_user": userID
    }
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer Replace API key Here",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)

getUserID()
getAssetID()
checkOutAsset()