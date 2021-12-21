import requests
import json
import sys

# get arguments from onboard script and pass them to variables
newUserName = str(sys.argv[1])
newUserEmail = str(sys.argv[1])
schoolSite = str(sys.argv[2])
firstName = str(sys.argv[3])
lastName = str(sys.argv[4])

# newUserName = "renetestAPI@coronacharter.org"
# newUserEmail = "renetestAPI@coronacharter.org"
# schoolSite = "BCCS"
# firstName = "Rene"
# lastName = "Sanchez"
url = "https://inventory.ypics.org/api/v1/users"

payload = {
    "first_name": "Renee",
    "last_name": "Sanchez",
    "username": "renee.api@coronacharter.org",
    "password": "R3setPWD!",
    "password_confirmation": "R3setPWD!",
    "email": "renee.api@coronacharter.org",
    "activated": True,
    "company_id": 1,
    "location_id": 5
}
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMTAzMzkwZjE5ZTA1MzU1ZTkwNWYwMjA5YmQwNDU0Mjk2ZTY4OTJmNzgwMDgzMWI5NWRhZjg1YzY4Yjc3YjIxYTY2NDNkMDM3NjYzOTU5ZTEiLCJpYXQiOjE2Mzg4NTQwNzMsIm5iZiI6MTYzODg1NDA3MywiZXhwIjoyOTAxMTU4MDczLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.aIuMRFw8zXLuV8EocIRsG5lsRNtPZlPQZQNFxY_sAtMJTLJypt2MJ1I900l0NO1olMYuH0l4KJkK1K6Z3Vf-Rb-xv6E7HQ4fsUNyedEyos3jTZSje6zBtUNsMYnYWPqSAZ8A2G7d7zA-g_8hJRC0oRvHPvTNiRCTdlZiFmDgJ7fAMTGlHLvoKHl0AOqNKLdAU0Ng1UCn3aftr_7GdalD6f15Atzf1_uzardePeeeebxnwnG10THrCivtVh4w3PPwUG6UZ88T0ImPVKmu2XVu0xkc_MX9-jSkYo96sryCWpcMU3IGWnAL7sFfJTFCyDbB7Qx6oIjfCJ_bhdV00bxligXuSoEmmdfXpELpexQVm2GuzrVB2Nw7Cd2wtGrx4GGi9c0lfYEXiMLVEVX6zP7KsGPyD7qWP3OUiqyO0TlEBezjWv2hbQ6GkpfDwCGMtuH6S5RJ9EsyQ_dmBumzORGsvKK8Ka_rYTyzp04ElO6qQpzFCYPxQ4KCYhJus8a3yYTNOcE2OOo4VTlG7q94W3uCYxsV06zwg0hGE7QfFtUqj0jGOrOXWJt2dtRTOkkOLcckjndQKBz0Kt3riXjgQk_A4siMyToY6q1m4MhSxDJwyTyuIhmiwKtkQ0Ed3jo1Pn8-l3DxALD7E_9_nfsotOl1JaoFiZWh50ruqs5Ji-mDv6Q",
    "Content-Type": "application/json"
}

###change form
payload["email"]= newUserEmail
payload["username"]= newUserName
payload["first_name"]= firstName
payload["last_name"]= lastName
if schoolSite == "BCCS":
    payload["location_id"]= 2
elif schoolSite == "MORCS":
    payload["location_id"]= 4
elif schoolSite == "BCCHS":
    payload["location_id"]= 3
else:
    payload["location_id"]= 5

response = requests.request("POST", url, json=payload, headers=headers)
json_data = json.loads(response.text)


print(json_data['status'] + "!" + " " + json_data['messages'])
# LSC ID = 5
# Staff department ID = 2
# department":{"id":2,"name":"Staff"}
# YPICS company ID = 1
# "jobtitle":"Teacher"
# location":{"id":2,"name":"BCCS"}
# location {"id":4,"name":"MORCS"}
# "location":{"id":3,"name":"BCCHS"}




#########################################################
#           Get request
# import requests

# url = "https://inventory.ypics.org/api/v1/users?limit=50&offset=0&sort=created_at&order=desc&username=mrsimonsen@coronacharter.org&deleted=false&all=false"

# headers = {
#     "Accept": "application/json",
#     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMTAzMzkwZjE5ZTA1MzU1ZTkwNWYwMjA5YmQwNDU0Mjk2ZTY4OTJmNzgwMDgzMWI5NWRhZjg1YzY4Yjc3YjIxYTY2NDNkMDM3NjYzOTU5ZTEiLCJpYXQiOjE2Mzg4NTQwNzMsIm5iZiI6MTYzODg1NDA3MywiZXhwIjoyOTAxMTU4MDczLCJzdWIiOiIxIiwic2NvcGVzIjpbXX0.aIuMRFw8zXLuV8EocIRsG5lsRNtPZlPQZQNFxY_sAtMJTLJypt2MJ1I900l0NO1olMYuH0l4KJkK1K6Z3Vf-Rb-xv6E7HQ4fsUNyedEyos3jTZSje6zBtUNsMYnYWPqSAZ8A2G7d7zA-g_8hJRC0oRvHPvTNiRCTdlZiFmDgJ7fAMTGlHLvoKHl0AOqNKLdAU0Ng1UCn3aftr_7GdalD6f15Atzf1_uzardePeeeebxnwnG10THrCivtVh4w3PPwUG6UZ88T0ImPVKmu2XVu0xkc_MX9-jSkYo96sryCWpcMU3IGWnAL7sFfJTFCyDbB7Qx6oIjfCJ_bhdV00bxligXuSoEmmdfXpELpexQVm2GuzrVB2Nw7Cd2wtGrx4GGi9c0lfYEXiMLVEVX6zP7KsGPyD7qWP3OUiqyO0TlEBezjWv2hbQ6GkpfDwCGMtuH6S5RJ9EsyQ_dmBumzORGsvKK8Ka_rYTyzp04ElO6qQpzFCYPxQ4KCYhJus8a3yYTNOcE2OOo4VTlG7q94W3uCYxsV06zwg0hGE7QfFtUqj0jGOrOXWJt2dtRTOkkOLcckjndQKBz0Kt3riXjgQk_A4siMyToY6q1m4MhSxDJwyTyuIhmiwKtkQ0Ed3jo1Pn8-l3DxALD7E_9_nfsotOl1JaoFiZWh50ruqs5Ji-mDv6Q"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)