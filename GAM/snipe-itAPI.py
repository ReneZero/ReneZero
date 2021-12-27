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
url = "https://YourSnipeITSiteHere/api/v1/users"

payload = {
    "first_name": "Renee",
    "last_name": "Sanchez",
    "username": "renee.api@coronacharter.org",
    "password": "PSSWORDHERE",
    "password_confirmation": "R3setPWD!",
    "email": "renee.api@coronacharter.org",
    "activated": True,
    "company_id": 1,
    "location_id": 5
}
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer PASTE API KEY HERE",
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


print((str(json_data['status'])) + "!" + " " + (str(json_data['messages'])))
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

# url = "https://YourSnipeItSiteHere.org/api/v1/users?limit=50&offset=0&sort=created_at&order=desc&username=mrsimonsen@coronacharter.org&deleted=false&all=false"

# headers = {
#     "Accept": "application/json",
#     "Authorization": "Bearer PASTE API KEY HERE"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)