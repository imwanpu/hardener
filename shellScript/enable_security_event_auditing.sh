#!/bin/bash
# enable_security_event_auditing.sh
# Enable security event auditing on Ubuntu 20.04 and CentOS 7

# Install auditd if not already installed
which auditctl &>/dev/null || {
    echo "Installing auditd..."
    apt-get install -y auditd || yum install -y auditd
}

# Enable and start auditd service
systemctl enable auditd
systemctl start auditd
