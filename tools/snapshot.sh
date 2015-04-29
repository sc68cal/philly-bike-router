#!/bin/sh
API="https://api.phila.gov/bike-share-stations/v1/"
while [ true ]
do
	curl $API > `date -u +%Y-%m-%d-%H-%M`.json
	if [ $(date -u +%H) -lt 11 ];then
		echo "Sleeping an hour"
		sleep 3600
	else
		sleep 900
	fi
done
