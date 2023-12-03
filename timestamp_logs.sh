#!/bin/bash

# Copy /var/log/syslog to the current working directory
cp /var/log/syslog .

# Get the current date and time
current_datetime=$(date +"%Y%m%d%H%M%S")

# Append the current date and time to the filename
new_filename="syslog_${current_datetime}.log"
mv syslog "$new_filename"
