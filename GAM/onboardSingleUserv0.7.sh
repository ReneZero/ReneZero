#!/usr/bin/env bash
# User Onloading

GAM=~/bin/gamadv-xtd3/gam

echo "PLease enter the staff's first name: "

read firstName

echo "Please enter staff's Lastname: "

read lastName

echo "Please enter the email you wish to give them: "

read staffEmail

start_logger() {
    exec &> >(tee onboard.log)
    echo "$(whoami) conducting onboarding for $staffEmail on $(date)"
}

email_verification() {
    echo "Checking to see if user exists"
    if ${GAM} info user "${staffEmail}" >/dev/null 2>&1; then
        printf %s\\n "Please try again and enter a valid email address. This one is already taken"
        exit 1
    else
        echo "$staffEmail does not exist in Google Suite. We are clear to proceed"
    fi
    printf %s\\n "Going to next step"

}

create_email() {
    echo "creating email for $staffEmail"
    ${GAM} create user "${staffEmail}"
    ${GAM} update user "${staffEmail}" givenname "${firstName}"
    ${GAM} update user "${staffEmail}" familyname "${lastName}"
    echo "succefully created user"
    
}


reset_password() {
    echo "Resetting GSuite password to R3setPWD!"
    PASSWORD=R3setPWD!
    ${GAM} update user "${staffEmail}" password "${PASSWORD}"
    ${GAM} update user "${staffEmail}" changepassword on
}

change_ou() {
    echo "Which site is staff working at? Please enter a number"
    echo -n "[1]BCCS [2]Morcs [3]BCCHS [4]LSC: "
    read VAR
if [[ $VAR -eq 1 ]]
then
  echo "changing to BCCS Staff OU"
  ${GAM} update org '/Staff/BCCS Staff' add users "${staffEmail}"
elif [[ $VAR -eq 2 ]]
then
  echo "changing to MORCS Staff OU"
  ${GAM} update org '/Staff/MORCS Staff' add users "${staffEmail}"
elif [[ $VAR -eq 3 ]]
then
  echo "changing to BCCHS Staff OU"
  ${GAM} update org '/Staff/BCCHS Staff' add users "${staffEmail}"
elif [[ $VAR -eq 4 ]]
then
  echo "changing to LSC Staff OU"
  ${GAM} update org '/Staff/LSC' add users "${staffEmail}"
else
  echo "did not enter a correct number"
  exit 1
fi

echo "is this a teacher or staff"
    echo -n "[1]Teacher [2]Staff [3]LSC: "
read TOF
if [[ $VAR -eq 1 && $TOF -eq 1 ]]
then
  echo "adding to BCCS Teachers Group & Assigning Admin Rights"
  ${GAM} update group bccsteachers@coronacharter.org add member "${staffEmail}"
${GAM} create admin "${staffEmail}" Teacher_Admin_Password_Reset_BCCS org_unit '/Students/BCCS Students'
elif [[ $VAR -eq 1 && $TOF -eq 2  ]]
then
  echo "What position is the staff member?"
    echo -n "[1]Tutor [2]scc [3]sped [4]afterschool [5]admin: "
    read POS
  if [[ $POS -eq 1 ]]; then
    echo "Moving to Tutor group"
    ${GAM} update group bccstutors@coronacharter.org add member "${staffEmail}"
elif [[ $POS -eq 2 ]]; then
    echo "moving to scc group"
  ${GAM} update group bccsscc@coronacharter.org add member "${staffEmail}"
elif [[ $POS -eq 3 ]]; then
    echo "moving to sped group"
  ${GAM} update group bccssped@coronacharter.org add member "${staffEmail}"
elif [[ $POS -eq 4 ]]; then
  echo "moving to afterschool group"
  ${GAM} update group bccsafterschool@coronacharter.org add member "${staffEmail}"
elif [[ $POS -eq 5 ]]; then
  echo "moving to admin group"
  ${GAM} update group bccsadmin@coronacharter.org add member "${staffEmail}"
else
   echo "did not enter a correct number"
  exit 1
fi
elif [[ $VAR -eq 2 && $TOF -eq 1 ]]
then
  echo "changing to Morcs Teachers Group & Assigning Admin Rights"
${GAM} update group morcsteachers@romerocharter.org add member "${staffEmail}"
${GAM} create admin "${staffEmail}" Teacher_Admin_Password_Reset_MORCS org_unit '/Students/MORCS Students'
elif [[ $VAR -eq 2 && $TOF -eq 2 ]]
then
  echo "What position is the staff member?"
    echo -n "[1]Tutor [2]scc [3]sped [4]afterschool [5]admin: "
    read POS
  if [[ $POS -eq 1 ]]; then
    echo "Moving to Tutor group"
    ${GAM} update group morcstutors@romerocharter.org add member "${staffEmail}"
elif [[ $POS -eq 2 ]]; then
    echo "moving to scc group"
  ${GAM} update group morcsscc@romerocharter.org add member "${staffEmail}"
elif [[ $POS -eq 3 ]]; then
    echo "moving to sped group"
  ${GAM} update group morcssped@romerocharter.org add member "${staffEmail}"
elif [[ $POS -eq 4 ]]; then
  echo "moving to afterschool group"
  ${GAM} update group morcsafterschool@romerocharter.org add member "${staffEmail}"
elif [[ $POS -eq 5 ]]; then
  echo "moving to admin group"
  ${GAM} update group morcsadmin@romerocharter.org add member "${staffEmail}"
else
   echo "did not enter a correct number"
  exit 1
fi
elif [[ $VAR -eq 3 && $TOF -eq 1 ]]
then
  echo "changing to BCCHS Teacher Group & Assigning Admin Rights"
${GAM} update group bcchsteachers@coronacharter.org add member "${staffEmail}"
${GAM} create admin "${staffEmail}" Teacher_Admin_Password_Reset_BCCHS org_unit '/Students/BCCHS Students'
elif [[ $VAR -eq 3 && $TOF -eq 2 ]]
then
  echo "What position is the staff member?"
    echo -n "[1]Tutor [2]scc [3]sped [4]afterschool [5]admin: "
    read POS
  if [[ $POS -eq 1 ]]; then
    echo "Moving to Tutor group"
    ${GAM} update group bcchstutors@coronacharter.org add member "${staffEmail}"
elif [[ $POS -eq 2 ]]; then
    echo "moving to scc group"
  ${GAM} update group bcchsscc@coronacharter.org add member "${staffEmail}"
elif [[ $POS -eq 3 ]]; then
    echo "moving to sped group"
  ${GAM} update group bcchssped@coronacharter.org add member "${staffEmail}"
elif [[ $POS -eq 4 ]]; then
  echo "moving to afterschool group"
  ${GAM} update group bcchsafterschool@coronacharter.org add member "${staffEmail}"
elif [[ $POS -eq 5 ]]; then
  echo "moving to admin group"
  ${GAM} update group bcchsadmin@coronacharter.org add member "${staffEmail}"
else
   echo "did not enter a correct number"
  exit 1
fi
elif [[ $VAR -eq 4 && $TOF -eq 3 ]]
then
  echo "changing to LSC Group"
${GAM} update group lsc@ypics.org add member "${staffEmail}"
else
  echo "did not enter a correct number"
  exit 1
fi
}

add_license() {
    echo "does this account need a enterprise license"
    echo -n "[1]Yes [2]No: "
    read VAR
if [[ $VAR -eq 1 ]]
then
  echo "Applying Education Plus License"
  ${GAM} user "${staffEmail}" add license 1010310002
elif [[ $VAR -eq 2 ]]
then
  echo "license skipped"
else
  echo "did not enter a correct number"
  exit 1
fi
}
add_Voicelicense() {
    echo "does this account need a Voice license"
    echo -n "[1]Yes [2]No: "
    read VAR
if [[ $VAR -eq 1 ]]
then
  echo "Applying Voice license"
  ${GAM} user "${staffEmail}" add license 1010330004
elif [[ $VAR -eq 2 ]]
then
  echo "license skipped"
else
  echo "did not enter a correct number"
  exit 1
fi
}


email_verification
start_logger
create_email
reset_password
change_ou
add_license
add_Voicelicense
