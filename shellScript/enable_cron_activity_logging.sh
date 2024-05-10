#!/bin/bash
# enable_cron_activity_logging.sh
# Enable logging for cron activities on Ubuntu 20.04 and CentOS 7

# Configure rsyslog to log cron activities
echo "Configuring rsyslog for cron logging..."
echo "cron.*                          /var/log/cron.log" >> /etc/rsyslog.d/50-default.conf
systemctl restart rsyslog
