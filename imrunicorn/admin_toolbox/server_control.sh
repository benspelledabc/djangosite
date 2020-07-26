#!/bin/bash

if [ $1 = "restart_gunicorn" ]; then
  # mkdir admin_toolbox/server_control_token
  # touch admin_toolbox/sampleFile
  # ping -c 3 google.com > admin_toolbox/google.ping
  touch admin_toolbox/restart_gunicorn.token
	if [ $? -eq 0 ]; then
    	echo "- GUNICORN: Successfully created restart token."
    	exit 0

	else
    	>&2 echo "- GUNICORN_ERROR: Failed creating restart token."
    	exit 1
	fi

elif [ $1 = "restart_nginx" ]
then
  # mkdir admin_toolbox/server_control_token
  # touch admin_toolbox/sampleFile
  # ping -c 3 google.com > admin_toolbox/google.ping
  touch admin_toolbox/restart_nginx.token
	if [ $? -eq 0 ]; then
    	echo "- NGINX: Successfully created restart token."
    	exit 0

	else
    	>&2 echo "- NGINX_ERROR: Failed creating restart token."
    	exit 1
	fi


elif [ $1 = "restart_gunicorn_and_nginx" ]
then
  # mkdir admin_toolbox/server_control_token
  # touch admin_toolbox/sampleFile
  # ping -c 3 google.com > admin_toolbox/google.ping
  touch admin_toolbox/restart_nginx.token
  touch admin_toolbox/restart_gunicorn.token
	if [ $? -eq 0 ]; then
    	echo "- GUNICORN_NGINX: Successfully created restart tokens."
    	exit 0

	else
    	>&2 echo "- GUNICORN_NGINX_ERROR: Failed creating restart tokens."
    	exit 1
	fi


elif [ $1 = "cancel_all_restarts" ]
then
  # mkdir admin_toolbox/server_control_token
  # touch admin_toolbox/sampleFile
  # ping -c 3 google.com > admin_toolbox/google.ping
  rm -rf admin_toolbox/restart_nginx.token
  rm -rf admin_toolbox/restart_gunicorn.token
	if [ $? -eq 0 ]; then
    	echo "- CANCEL: Successfully deleted all tokens."
    	exit 0

	else
    	>&2 echo "- CANCEL_ERROR: Failed deleting all tokens."
    	exit 1
	fi


else
  echo "Invalid argument"
  exit 1

fi