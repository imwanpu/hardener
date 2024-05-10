#!/bin/bash
# set_ttl_count.sh
# Set TTL settings for network packets on Ubuntu 20.04 and CentOS 7

# Apply TTL settings through sysctl
echo "net.ipv4.ip_default_ttl=64" >> /etc/sysctl.conf
sysctl -p
