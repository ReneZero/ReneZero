import requests
import json
import sys

assetTag = str(sys.argv[1])
assetID = "0"

####Get asset ID by Asset Tag
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
    
    
def checkInAsset():
    #####Checkin Asset Using Asset ID
    url = "https://inventory.ypics.org/api/v1/hardware/" + str(assetID) + "/checkin"

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer Replace API key Here",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, headers=headers)
    print(response.text)

getAssetID()
checkInAsset()
    

