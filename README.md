- 👋 Hi, I’m @ReneZero
- 🌱 I’m currently learning everything...
- 📫 How to reach me rene.sanchez@themill.com...

All of these scripts require GAM in order to work so make sure that is installed first you can find the guide here
https://github.com/GAM-team/GAM

Also you will need to Install the Python Requirements which you can do so by openeing the project in terminal and running 
**pip intall -r requirements.txt**


**-OffboardSingleUser** is a GAM script we use when a staff member leaves midway through the year randomly. This script will remove them from the google directory change their password to a random generated password, suspend the account and move them to a suspended OU. This will also delete their user In mosyle as well and also check in any devices that they had checked out to them in Mosyle and Snipe IT 

**-OffBoard.csv** is a GAM script we use when offbaording staff or teachers during summer. You must create a csv file where you have a header that says email in order for the script to read the data from that collum. This only has google features so far no implemnation of Mosyle or Snipe IT

**-onboardSingleUser** is also a GAM script that we use for our domain you can edit the portion that moves the user to the path of the OrgUnit and it should work for your orginization. This Creates the user for Gsuite, Moysle and SnipeIT. It can also check out devices and make sure it checks out the device to the user in mosyle and in SnipeIT.
