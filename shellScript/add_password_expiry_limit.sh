#!/bin/bash
# add_password_expiry_limit.sh
# Set password expiry on Ubuntu 20.04 and CentOS 7

# Edit login.defs to set password expiry
sed -i '/^PASS_MAX_DAYS/ s/.*/PASS_MAX_DAYS   90/' /etc/login.defs
sed -i '/^PASS_MIN_DAYS/ s/.*/PASS_MIN_DAYS   10/' /etc/login.defs
sed -i '/^PASS_WARN_AGE/ s/.*/PASS_WARN_AGE   7/' /etc/login.defs
