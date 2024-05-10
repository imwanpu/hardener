#!/bin/bash
# set_login_timeout_system_clock.sh
# Set login timeout and configure system clock on Ubuntu 20.04 and CentOS 7

# Set TMOUT for automatic logout on inactivity
echo "export TMOUT=900" >> /etc/profile
echo "Setting system clock to UTC..."
timedatectl set-timezone UTC
