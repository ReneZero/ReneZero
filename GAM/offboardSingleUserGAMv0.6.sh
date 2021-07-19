#!/usr/bin/env bash
# User Offboarding Script

# Initialize the full path of GAM
GAM=~/bin/gamadv-xtd3/gam

# Get Command line arguments for Employee Email and Term Type
POSITIONAL=()
while [[ $# -gt 0 ]]; do
    key="$1"

    case $key in
    -e | --email)
        EMPLOYEE="$2"
        shift # past argument
        shift # past value
        ;;
    -t | --termtype)
        TERMTYPE="$2"
        shift # past argument
        shift # past value
        ;;
    *) # unknown option
        POSITIONAL+=("$1") # save it in an array for later
        shift              # past argument
        ;;
    esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters

# Verify user exists in Google Suite
email_verification() {
    echo "Checking to see if user exists"
    if ${GAM} info user "${EMPLOYEE}" >/dev/null 2>&1; then
        return
    else
        echo "$EMPLOYEE does not exist in Google Suite."
    fi
    printf %s\\n "Please enter a valid email address."
    exit 1
}

# Create log file and record user information
start_logger() {
    exec &> >(tee offboard.log)
    echo "$(whoami) conducting offboarding for $EMPLOYEE on $(date)"
}

# Get the username and last name of employee
get_name() {
    USER_NAME="${EMPLOYEE//@coronacharter.org/}"
    LAST_NAME=$(echo "$USER_NAME" | cut -f2 -d'.')
}


reset_password() {
    echo "Resetting GSuite password"
    PASSWORD=$(openssl rand -base64 12)
    ${GAM} update user "${EMPLOYEE}" password "${PASSWORD}"
    ${GAM} update user "${EMPLOYEE}" changepassword on
    sleep 2
    ${GAM} update user "${EMPLOYEE}" changepassword off
}

# Remove all App-Specific account passwords, delete MFA Recovery Codes,
# Delete all OAuth tokens
# Generating new set of MFA recovery codes for the user
reset_token() {
    echo "Resetting GSuite tokens"
    ${GAM} user "${EMPLOYEE}" deprovision
    ${GAM} user "${EMPLOYEE}" update backupcodes
}

# Remove all email delegation
remove_delegates() {
    echo "Removing email delegates"
    DELEGATES=$(${GAM} user "${EMPLOYEE}" print delegates)
    for DELEGATE in "${DELEGATES[@]}"; do
        ${GAM} user "${EMPLOYEE}" delete delegate "${DELEGATE}"
    done
}

# Wipe device profile and remove Google accounts from all mobile devices
wipe_devices() {
    echo "Wiping all associated mobile devices"
    $GAM print mobile query "email:$EMPLOYEE" >>/tmp/tmp.mobile-data.csv
    $GAM csv /tmp/tmp.mobile-data.csv gam update mobile ~resourceId action account_wipe
} 

# Remove all forwarding addresses
# Disable IMAP
# Disable POP
# Hide user from directory
disable_user() {
    echo "Disabling Email and hiding from Directory"
    $GAM user "${EMPLOYEE}" forward off
    $GAM user "${EMPLOYEE}" imap off
    $GAM user "${EMPLOYEE}" pop off
    $GAM update user "${EMPLOYEE}" gal off
}

remove_license() {
    echo "Removing Education Plus License & OR Google Voice License"
    ${GAM} user "${EMPLOYEE}" delete license 1010310002
    ${GAM} user "${EMPLOYEE}" delete license 1010330004
}


# Remove the employee from all groups
remove_groups() {
    echo "Removing user from all groups"
    ${GAM} info user "${EMPLOYEE}" | grep -A 10000 "Groups:" | grep -i -o '[A-Z0-9._%+-]\+@[A-Z0-9.-]\+\.[A-Z]\{2,4\}' >/tmp/"${EMPLOYEE}".txt
    while read -r GROUP; do
        [ -z "$GROUP" ] && continue
        ${GAM} update group "${GROUP}" remove member "${EMPLOYEE}"
    done </tmp/"${EMPLOYEE}".txt
}
# Remove admin privledges from all groups
remove_AdminRights() {
    echo "Removing admin Rights from " $EMPLOYEE
    ${GAM} print admins user "${EMPLOYEE}" | ${GAM} csv - gam delete admin ~roleAssignmentId
}


# Delegate email access to manager if termination is Involuntary
# Suspend user to kick off all logged in sessions
# Unsuspend Involuntary termination user for email delgation
# Verify that user was moved to correct Organizational Unit
suspend_user() {
    ${GAM} update user "${EMPLOYEE}" suspended on
        echo "Suspending user and moving to z-Archive OU"
        ${GAM} update org 'Suspended' add users "${EMPLOYEE}"
    ORG_UNIT=$(${GAM} info user "${EMPLOYEE}" | grep "Google Org")
    echo "$EMPLOYEE moved to $ORG_UNIT"
}

# Main
start_logger
email_verification
get_name
reset_password
reset_token
disable_user
remove_groups
suspend_user
remove_AdminRights
remove_license
