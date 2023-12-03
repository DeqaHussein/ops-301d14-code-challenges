#!/bin/bash

# Print file size before compression
echo "File size before compression:"
du -h /var/log/syslog /var/log/wtmp

# Backup directory
backup_dir="/var/log/backups"

# Create the backup directory if it doesn't exist
mkdir -p "$backup_dir"

# Compress and timestamp the log files
timestamp=$(date +"%Y%m%d%H%M%S")
gzip -c /var/log/syslog > "$backup_dir/syslog-$timestamp.zip"
gzip -c /var/log/wtmp > "$backup_dir/wtmp-$timestamp.zip"

# Clear the contents of the log files
cat /dev/null > /var/log/syslog
cat /dev/null > /var/log/wtmp

# Print file size after compression
echo "File size after compression:"
du -h "$backup_dir/syslog-$timestamp.zip" "$backup_dir/wtmp-$timestamp.zip"

# Compare file sizes
echo "Comparison of file sizes:"
du -h /var/log/syslog /var/log/wtmp "$backup_dir/syslog-$timestamp.zip" "$backup_dir/wtmp-$timestamp.zip"
