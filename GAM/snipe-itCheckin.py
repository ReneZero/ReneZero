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
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMTAzMzkwZjE5ZTA1MzU1ZTkwNWYwMjA5YmQwNDU0Mjk2ZTY4OTJmNzgwMDgzMWI5NWRhZjg1YzY4Yjc3YjIxYTY2NDNkMDM3NjYzOTU5ZTEiLCJpYXQiOjE2Mzg4NTQwNzMsIm5iZiI6MTYzODg1NDA3MywiZXhwIjoyOTAxMTU4MDczLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.aIuMRFw8zXLuV8EocIRsG5lsRNtPZlPQZQNFxY_sAtMJTLJypt2MJ1I900l0NO1olMYuH0l4KJkK1K6Z3Vf-Rb-xv6E7HQ4fsUNyedEyos3jTZSje6zBtUNsMYnYWPqSAZ8A2G7d7zA-g_8hJRC0oRvHPvTNiRCTdlZiFmDgJ7fAMTGlHLvoKHl0AOqNKLdAU0Ng1UCn3aftr_7GdalD6f15Atzf1_uzardePeeeebxnwnG10THrCivtVh4w3PPwUG6UZ88T0ImPVKmu2XVu0xkc_MX9-jSkYo96sryCWpcMU3IGWnAL7sFfJTFCyDbB7Qx6oIjfCJ_bhdV00bxligXuSoEmmdfXpELpexQVm2GuzrVB2Nw7Cd2wtGrx4GGi9c0lfYEXiMLVEVX6zP7KsGPyD7qWP3OUiqyO0TlEBezjWv2hbQ6GkpfDwCGMtuH6S5RJ9EsyQ_dmBumzORGsvKK8Ka_rYTyzp04ElO6qQpzFCYPxQ4KCYhJus8a3yYTNOcE2OOo4VTlG7q94W3uCYxsV06zwg0hGE7QfFtUqj0jGOrOXWJt2dtRTOkkOLcckjndQKBz0Kt3riXjgQk_A4siMyToY6q1m4MhSxDJwyTyuIhmiwKtkQ0Ed3jo1Pn8-l3DxALD7E_9_nfsotOl1JaoFiZWh50ruqs5Ji-mDv6Q"
    }

    response = requests.request("GET", url, headers=headers)

    json_data = json.loads(response.text)

    assetID = json_data['id']
    
    
def checkInAsset():
    #####Checkin Asset Using Asset ID
    url = "https://inventory.ypics.org/api/v1/hardware/" + str(assetID) + "/checkin"

    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMTAzMzkwZjE5ZTA1MzU1ZTkwNWYwMjA5YmQwNDU0Mjk2ZTY4OTJmNzgwMDgzMWI5NWRhZjg1YzY4Yjc3YjIxYTY2NDNkMDM3NjYzOTU5ZTEiLCJpYXQiOjE2Mzg4NTQwNzMsIm5iZiI6MTYzODg1NDA3MywiZXhwIjoyOTAxMTU4MDczLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.aIuMRFw8zXLuV8EocIRsG5lsRNtPZlPQZQNFxY_sAtMJTLJypt2MJ1I900l0NO1olMYuH0l4KJkK1K6Z3Vf-Rb-xv6E7HQ4fsUNyedEyos3jTZSje6zBtUNsMYnYWPqSAZ8A2G7d7zA-g_8hJRC0oRvHPvTNiRCTdlZiFmDgJ7fAMTGlHLvoKHl0AOqNKLdAU0Ng1UCn3aftr_7GdalD6f15Atzf1_uzardePeeeebxnwnG10THrCivtVh4w3PPwUG6UZ88T0ImPVKmu2XVu0xkc_MX9-jSkYo96sryCWpcMU3IGWnAL7sFfJTFCyDbB7Qx6oIjfCJ_bhdV00bxligXuSoEmmdfXpELpexQVm2GuzrVB2Nw7Cd2wtGrx4GGi9c0lfYEXiMLVEVX6zP7KsGPyD7qWP3OUiqyO0TlEBezjWv2hbQ6GkpfDwCGMtuH6S5RJ9EsyQ_dmBumzORGsvKK8Ka_rYTyzp04ElO6qQpzFCYPxQ4KCYhJus8a3yYTNOcE2OOo4VTlG7q94W3uCYxsV06zwg0hGE7QfFtUqj0jGOrOXWJt2dtRTOkkOLcckjndQKBz0Kt3riXjgQk_A4siMyToY6q1m4MhSxDJwyTyuIhmiwKtkQ0Ed3jo1Pn8-l3DxALD7E_9_nfsotOl1JaoFiZWh50ruqs5Ji-mDv6Q",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, headers=headers)
    print(response.text)

getAssetID()
checkInAsset()
    

