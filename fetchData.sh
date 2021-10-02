#!/bin/bash

query="https://www.space-track.org/basicspacedata/query/class/gp/format/json"

if ( [ -z "$1" ] || [ -z "$2" ] ); then
	echo -n "Login:"
	read login
	echo -n Password: 
	read -s password
else
	login=$1
	password=$2
fi
curl https://www.space-track.org/ajaxauth/login -d "identity=$login&password=$password&query=$query" > result.json

result=`head -n 1 result.json`
error='{"Login":"Password does not meet minimum length requirements."}'
error2='{"error":"You must be logged in to complete this action"}'
if [ "$result" != "$error" ] && [ "$result" != "$error2" ]; then
	echo "Loading Successfull"
	echo $result
else
    echo "Login or password are wrong."
fi