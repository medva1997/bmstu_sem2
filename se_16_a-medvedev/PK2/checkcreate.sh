#!/bin/bash
while inotifywait -e create /home/alexey/original_video/; do
	#python3 /var/www/html/prepvideo.py
	echo 'worked'
done
original_video


inotifywait -m -r -q --format '%f' bootstrap/ | while read FILE
do
  echo "something happened on path $FILE"
done