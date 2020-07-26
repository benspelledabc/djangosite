#!/bin/bash

if [ $1 = "create" ]; then
        mkdir admin_toolbox/server_control_token
        # touch admin_toolbox/sampleFile
        # ping -c 3 google.com > admin_toolbox/google.ping
	if [ $? -eq 0 ]; then
    	echo "-Successfully  created directory"
    	exit 0

	else
    	>&2 echo "Error: Failed creating directory"
    	exit 1
	fi

elif [ $1 = "delete" ]
then
   	rm -rf admin_toolbox/server_control_token
   	# rm -rf admin_toolbox/sampleFile
   	# ping -c 1 google.com > admin_toolbox/google.ping
        if [ $? -eq 0 ]; then
        echo "-Successfully deleted directory"
        exit 0

        else
        >&2 echo "Error: Failed deleting directory"
        exit 1
        fi

else
  echo "Invalid argument"
  exit 1

fi