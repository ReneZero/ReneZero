#!/usr/bin/env bash


GAM=~/bin/gamadv-xtd3/gam

start_logger() {
    exec &> >(tee MovingGroups.log)
    echo "$(whoami) conducting moving of groups on $(date)"
}
echo '
##      ##    ###    ########  ##    ## #### ##    ##  ######   
##  ##  ##   ## ##   ##     ## ###   ##  ##  ###   ## ##    ##  
##  ##  ##  ##   ##  ##     ## ####  ##  ##  ####  ## ##        
##  ##  ## ##     ## ########  ## ## ##  ##  ## ## ## ##   #### 
##  ##  ## ######### ##   ##   ##  ####  ##  ##  #### ##    ##  
##  ##  ## ##     ## ##    ##  ##   ###  ##  ##   ### ##    ##  
 ###  ###  ##     ## ##     ## ##    ## #### ##    ##  ######   
'
echo "Welcome to the moving groups script"
echo "Which school site would you like to do first? Please enter a number"
echo -n "[1]BCCS [2]Morcs [3]BCCHS: "
read SCHOOL
	if [[ $SCHOOL -eq 1 ]]; then
		echo -n "Are you sure you want to proceed ? [1]Yes [2]NO: "
		read YON
		if [[ $YON -eq 2 ]]; then
			echo "Goodbye"
			exit 1
		elif [[ $YON -eq 1 ]]; then
			echo "Continuing"
		else
			echo "did not enter a valid number, Goodbye"
		fi
		echo "making csv file"
		${GAM} print group-members group 8thgrade@coronacharter.org > ./8thgradeBCCS.csv
echo "Removing graduated 8th graders"
		${GAM} csv ./8thgradeBCCS.csv gam update group 8thgrade@coronacharter.org delete user "~email"
#removing 8thgradefile
	rm ./8thgradeBCCS
		${GAM} print group-members group 7thgrade@coronacharter.org > ./7thgradeTo8thGradeBCCS.csv
	echo "moving 7th grade to 8th grade"
		${GAM} csv ./7thgradeTo8thGradeBCCS.csv gam update group 8thgrade@coronacharter.org add user "~email"
	echo "moving old 7th graders out of 7thgrade group"
		${GAM} csv ./7thgradeTo8thGradeBCCS.csv gam update group 7thgrade@coronacharter.org delete user "~email"
		${GAM} print group-members group 6thgrade@coronacharter.org > ./6thgradeTo7thGradeBCCS.csv
	echo "moving 6th grade to 7th grade"
		${GAM} csv ./6thgradeTo7thGradeBCCS.csv gam update group 7thgrade@coronacharter.org add user "~email"
	echo "moving old 6th graders out of 6th grade group"
	${GAM} csv ./6thgradeTo7thGradeBCCS.csv gam update group 6thgrade@coronacharter.org delete user "~email"
	${GAM} print orgs
	echo "Please copy and paste OU above of the incoming 6th graders"
	echo "example should look like this /Students/BCCHS Students/BCCHS 9th Grade/BCCHS 2025"
	echo "paste the OU here: "
	Read OU
		${GAM} print users query "orgUnitPath='${OU}'" fields primaryemail > ./OUemails.csv
	echo "moving new incoming 6th graders to 6thgrade group"
		${GAM} csv ./OUemails.csv gam update group 6thgrade@coronacharter.org add user "~email"
	rm ./7thgradeTo8thGradeBCCS.csv
	rm ./6thgradeTo7thGradeBCCS.csv
	rm ./OUemails.csv
		echo "All done please re-run script for other sites"
	exit 1
elif [[ $SCHOOL -eq 2 ]]; then
	echo -n "Are you sure you want to proceed ? [1]Yes [2]NO"
		read YON
		if [[ $YON -eq 2 ]]; then
			echo "Goodbye"
			exit 1
		elif [[ $YON -eq 1 ]]; then
			echo "Continuing"
		else
			echo "did not enter a valid number, Goodbye"
		fi
	echo "making csv file"
		${GAM} print group-members group 8thgrade@romerocharter.org > ./8thgradeMORCS.csv
echo "Removing graduated 8th graders"
		${GAM} csv ./8thgradeMORCS.csv gam update group 8thgrade@romerocharter.org delete user "~email"
#removing 8thgradefile
	rm ./8thgradeMORCS
		${GAM} print group-members group 7thgrade@romerocharter.org > ./7thgradeTo8thGradeMORCS.csv
	echo "moving 7th grade to 8th grade"
		${GAM} csv ./7thgradeTo8thGradeMORCS.csv gam update group 8thgrade@romerocharter.org add user "~email"
	echo "moving old 7th graders out of 7thgrade group"
		${GAM} csv ./7thgradeTo8thGradeMORCS.csv gam update group 7thgrade@romerocharter.org delete user "~email"
		${GAM} print group-members group 6thgrade@romerocharter.org > ./6thgradeTo7thGradeMORCS.csv
	echo "moving 6th grade to 7th grade"
		${GAM} csv ./6thgradeTo7thGradeMORCS.csv gam update group 7thgrade@romerocharter.org add user "~email"
	echo "moving old 6th graders out of 6th grade group"
	${GAM} csv ./6thgradeTo7thGradeMORCS.csv gam update group 6thgrade@romerocharter.org delete user "~email"

	${GAM} print orgs
	echo "Please copy and paste OU above of the incoming 6th graders"
	echo "example should look like this /Students/BCCHS Students/BCCHS 9th Grade/BCCHS 2025"
	echo "paste the OU here: "
	Read OU
		${GAM} print users query "orgUnitPath='${OU}'" fields primaryemail > ./OUemailsMorcs.csv
	echo "moving new incoming 6th graders to 6thgrade group"
		${GAM} csv ./OUemails.csv gam update group 6thgrade@coronacharter.org add user "~email"
	echo "All done please re-run script for other sites"
	exit 1
elif [[ $SCHOOL -eq 3 ]]; then
	echo -n "Are you sure you want to proceed ? [1]Yes [2]NO"
		read YON
		if [[ $YON -eq 2 ]]; then
			echo "Goodbye"
			exit 1
		elif [[ $YON -eq 1 ]]; then
			echo "Continuing"
		else
			echo "did not enter a valid number, Goodbye"
		fi
	echo "making csv file"
		${GAM} print group-members group 12thgrade@coronacharter.org > ./12thgrade.csv
echo "Removing graduated 12th graders"
		${GAM} csv ./12thgrade.csv gam update group 12thgrade@coronacharter.org delete user "~email"
#removing 12thgrade file.
	rm ./12thgrade.csv
		${GAM} print group-members group 11thgrade@coronacharter.org > ./11thgradeTo12thGrade.csv
	echo "moving 11th grade to 12th grade"
		${GAM} csv ./11thgradeTo12thGrade.csv gam update group 12thgrade@coronacharter.org add user "~email"
	echo "moving old 11th graders out of 11thgrade group"
		${GAM} csv ./11thgradeTo12thGrade.csv gam update group 11thgrade@coronacharter.org delete user "~email"
		${GAM} print group-members group 10thgrade@coronacharter.org > ./10thgradeTo11thGrade.csv
	echo "moving 10th grade to 11th grade"
		${GAM} csv ./10thgradeTo11thGrade.csv gam update group 11thgrade@coronacharter.org add user "~email"
	echo "moving old 10th graders out of 10thgrade group"
		${GAM} csv ./10thgradeTo11thGrade.csv gam update group 10thgrade@coronacharter.org delete user "~email"
		${GAM} print group-members group 9thgrade@coronacharter.org > ./9thgradeTo10thGrade.csv
	echo "moving 9th grade to 10th grade"
		${GAM} csv ./9thgradeTo10thGrade.csv gam update group 10thgrade@coronacharter.org add user "~email"
	echo "moving old 6th graders out of 6th grade group"
	${GAM} csv ./9thgradeTo10thGrade.csv gam update group 9thgrade@coronacharter.org delete user "~email"

	${GAM} print orgs
	echo "Please copy and paste OU above of the incoming 6th graders"
	echo "example should look like this /Students/BCCHS Students/BCCHS 9th Grade/BCCHS 2025"
	echo "paste the OU here: "
	read OU
		${GAM} print users query "orgUnitPath='${OU}'" fields primaryemail > ./OUemailsMorcs.csv
	echo "moving new incoming 9th graders to 9thgrade group"
		${GAM} csv ./OUemails.csv gam update group 9thgrade@coronacharter.org add user "~email"
	echo "All done please re-run script for other sites"
	exit 1
	fi
