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
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMTAzMzkwZjE5ZTA1MzU1ZTkwNWYwMjA5YmQwNDU0Mjk2ZTY4OTJmNzgwMDgzMWI5NWRhZjg1YzY4Yjc3YjIxYTY2NDNkMDM3NjYzOTU5ZTEiLCJpYXQiOjE2Mzg4NTQwNzMsIm5iZiI6MTYzODg1NDA3MywiZXhwIjoyOTAxMTU4MDczLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.aIuMRFw8zXLuV8EocIRsG5lsRNtPZlPQZQNFxY_sAtMJTLJypt2MJ1I900l0NO1olMYuH0l4KJkK1K6Z3Vf-Rb-xv6E7HQ4fsUNyedEyos3jTZSje6zBtUNsMYnYWPqSAZ8A2G7d7zA-g_8hJRC0oRvHPvTNiRCTdlZiFmDgJ7fAMTGlHLvoKHl0AOqNKLdAU0Ng1UCn3aftr_7GdalD6f15Atzf1_uzardePeeeebxnwnG10THrCivtVh4w3PPwUG6UZ88T0ImPVKmu2XVu0xkc_MX9-jSkYo96sryCWpcMU3IGWnAL7sFfJTFCyDbB7Qx6oIjfCJ_bhdV00bxligXuSoEmmdfXpELpexQVm2GuzrVB2Nw7Cd2wtGrx4GGi9c0lfYEXiMLVEVX6zP7KsGPyD7qWP3OUiqyO0TlEBezjWv2hbQ6GkpfDwCGMtuH6S5RJ9EsyQ_dmBumzORGsvKK8Ka_rYTyzp04ElO6qQpzFCYPxQ4KCYhJus8a3yYTNOcE2OOo4VTlG7q94W3uCYxsV06zwg0hGE7QfFtUqj0jGOrOXWJt2dtRTOkkOLcckjndQKBz0Kt3riXjgQk_A4siMyToY6q1m4MhSxDJwyTyuIhmiwKtkQ0Ed3jo1Pn8-l3DxALD7E_9_nfsotOl1JaoFiZWh50ruqs5Ji-mDv6Q"
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
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMTAzMzkwZjE5ZTA1MzU1ZTkwNWYwMjA5YmQwNDU0Mjk2ZTY4OTJmNzgwMDgzMWI5NWRhZjg1YzY4Yjc3YjIxYTY2NDNkMDM3NjYzOTU5ZTEiLCJpYXQiOjE2Mzg4NTQwNzMsIm5iZiI6MTYzODg1NDA3MywiZXhwIjoyOTAxMTU4MDczLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.aIuMRFw8zXLuV8EocIRsG5lsRNtPZlPQZQNFxY_sAtMJTLJypt2MJ1I900l0NO1olMYuH0l4KJkK1K6Z3Vf-Rb-xv6E7HQ4fsUNyedEyos3jTZSje6zBtUNsMYnYWPqSAZ8A2G7d7zA-g_8hJRC0oRvHPvTNiRCTdlZiFmDgJ7fAMTGlHLvoKHl0AOqNKLdAU0Ng1UCn3aftr_7GdalD6f15Atzf1_uzardePeeeebxnwnG10THrCivtVh4w3PPwUG6UZ88T0ImPVKmu2XVu0xkc_MX9-jSkYo96sryCWpcMU3IGWnAL7sFfJTFCyDbB7Qx6oIjfCJ_bhdV00bxligXuSoEmmdfXpELpexQVm2GuzrVB2Nw7Cd2wtGrx4GGi9c0lfYEXiMLVEVX6zP7KsGPyD7qWP3OUiqyO0TlEBezjWv2hbQ6GkpfDwCGMtuH6S5RJ9EsyQ_dmBumzORGsvKK8Ka_rYTyzp04ElO6qQpzFCYPxQ4KCYhJus8a3yYTNOcE2OOo4VTlG7q94W3uCYxsV06zwg0hGE7QfFtUqj0jGOrOXWJt2dtRTOkkOLcckjndQKBz0Kt3riXjgQk_A4siMyToY6q1m4MhSxDJwyTyuIhmiwKtkQ0Ed3jo1Pn8-l3DxALD7E_9_nfsotOl1JaoFiZWh50ruqs5Ji-mDv6Q"
    }

    response = requests.request("GET", url, headers=headers)

    json_data = json.loads(response.text)
## grab user data info from the list rows into a string 
    userData = str(json_data['rows'])
    ### parse the user data string from the 8-11th character to grab the user ID
    ## we had to do this since the rows table just has one index with a huge string
    userID = userData[8:11]
        

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
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMTAzMzkwZjE5ZTA1MzU1ZTkwNWYwMjA5YmQwNDU0Mjk2ZTY4OTJmNzgwMDgzMWI5NWRhZjg1YzY4Yjc3YjIxYTY2NDNkMDM3NjYzOTU5ZTEiLCJpYXQiOjE2Mzg4NTQwNzMsIm5iZiI6MTYzODg1NDA3MywiZXhwIjoyOTAxMTU4MDczLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.aIuMRFw8zXLuV8EocIRsG5lsRNtPZlPQZQNFxY_sAtMJTLJypt2MJ1I900l0NO1olMYuH0l4KJkK1K6Z3Vf-Rb-xv6E7HQ4fsUNyedEyos3jTZSje6zBtUNsMYnYWPqSAZ8A2G7d7zA-g_8hJRC0oRvHPvTNiRCTdlZiFmDgJ7fAMTGlHLvoKHl0AOqNKLdAU0Ng1UCn3aftr_7GdalD6f15Atzf1_uzardePeeeebxnwnG10THrCivtVh4w3PPwUG6UZ88T0ImPVKmu2XVu0xkc_MX9-jSkYo96sryCWpcMU3IGWnAL7sFfJTFCyDbB7Qx6oIjfCJ_bhdV00bxligXuSoEmmdfXpELpexQVm2GuzrVB2Nw7Cd2wtGrx4GGi9c0lfYEXiMLVEVX6zP7KsGPyD7qWP3OUiqyO0TlEBezjWv2hbQ6GkpfDwCGMtuH6S5RJ9EsyQ_dmBumzORGsvKK8Ka_rYTyzp04ElO6qQpzFCYPxQ4KCYhJus8a3yYTNOcE2OOo4VTlG7q94W3uCYxsV06zwg0hGE7QfFtUqj0jGOrOXWJt2dtRTOkkOLcckjndQKBz0Kt3riXjgQk_A4siMyToY6q1m4MhSxDJwyTyuIhmiwKtkQ0Ed3jo1Pn8-l3DxALD7E_9_nfsotOl1JaoFiZWh50ruqs5Ji-mDv6Q",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)

getUserID()
getAssetID()
checkOutAsset()