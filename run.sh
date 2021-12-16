#!/bin/bash


# script is launched periodically isung systemd
# see: https://wiki.ubuntuusers.de/systemd/Timer_Units/
# https://askubuntu.com/questions/844533/how-to-execute-a-script-periodically-without-using-crontab

# switch to directory where this file is located
cd "$(dirname "$0")" 

# check for code updates
echo "Checking for Updates"
git pull

# run program
python3 src/main.py