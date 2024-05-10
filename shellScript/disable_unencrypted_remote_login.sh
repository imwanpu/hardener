#!/bin/bash
# disable_unencrypted_remote_login.sh
# Disable unencrypted remote login protocols on Ubuntu 20.04 and CentOS 7

# Disable telnet
echo "Disabling Telnet..."
systemctl stop telnet.socket
systemctl disable telnet.socket
