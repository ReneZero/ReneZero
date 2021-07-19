#!/usr/bin/env bash
# User Offboarding Script

GAM=~/bin/gamadv-xtd3/gam

start_logger() {
    exec &> >(tee offboard.log)
    echo "$(whoami) conducting offboarding on $(date)"
}

suspend_user() {
    ${GAM} csv $csvFile gam update user "~email" suspended on
        echo "Suspending user and moving to z-Archive OU"
        ${GAM} csv $csvFile gam update org 'Suspended' add users "~email"
        echo "Suspending"
}
reset_password() {
    echo "Resetting GSuite password"
    PASSWORD=$(openssl rand -base64 12)
    ${GAM} update user "~email" password "${PASSWORD}"
    ${GAM} update user "~email"changepassword on
    sleep 2
    ${GAM} update user "~email" changepassword off
}

disable_user() {
    echo "Disabling Email and hiding from Directory"
    ${GAM} csv $csvFile gam user "~email" forward off
    ${GAM} csv $csvFile gam user "~email" imap off
    ${GAM} csv $csvFile gam user "~email" pop off
    ${GAM} csv $csvFile gam update user "~email" gal off
}
remove_license() {
    echo "Removing Education Plus License & OR Google Voice License"
    ${GAM} csv $csvFile gam user "~email" delete license 1010310002
    ${GAM} csv $csvFile gam user "~email" delete license 1010330004
}

remove_groups() {
    echo "Removing user from all groups"
    ${GAM} csv $csvFile gam info user "~email" | grep -A 10000 "Groups:" | grep -i -o '[A-Z0-9._%+-]\+@[A-Z0-9.-]\+\.[A-Z]\{2,4\}' >/tmp/remove.txt
    while read -r GROUP; do 
        [ -z "$GROUP" ] && continue
        ${GAM} csv $csvFile gam update group "${GROUP}" remove member "~email"
    done </tmp/remove.txt
}
reset_token() {
    echo "Resetting GSuite tokens"
    ${GAM} user "~email" deprovision
    ${GAM} user "~email" update backupcodes
}
# Remove admin privledges from all groups
remove_AdminRights() {
    echo "Removing admin Rights"
    ${GAM} print admins user "~email" | ${GAM} csv - gam delete admin ~roleAssignmentId
}

echo "Please drag csv file here: "

read csvFile

start_logger
remove_groups
reset_token
disable_user
remove_license
suspend_user
remove_AdminRights
