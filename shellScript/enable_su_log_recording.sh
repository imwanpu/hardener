#!/bin/bash
# enable_su_log_recording.sh
# Enable logging for su command on Ubuntu 20.04 and CentOS 7

# Common PAM configuration for su
echo "Enabling su logging..."
if [[ -e /etc/pam.d/su ]]; then
    echo "session    required   pam_unix.so" >> /etc/pam.d/su
fi
