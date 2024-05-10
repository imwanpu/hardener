#!/bin/bash
# add_account_lock_policy.sh
# Set account lock policy after failed login attempts on Ubuntu 20.04 and CentOS 7

# Common PAM configuration
if [[ -e /etc/pam.d/common-auth ]]; then
    echo "Setting account lock policy on Ubuntu..."
    echo "auth required pam_tally2.so onerr=fail deny=5 unlock_time=1800" >> /etc/pam.d/common-auth
fi

if [[ -e /etc/pam.d/system-auth ]]; then
    echo "Setting account lock policy on CentOS..."
    echo "auth required pam_faillock.so preauth silent deny=5 unlock_time=1800" >> /etc/pam.d/system-auth
    echo "auth [default=die] pam_faillock.so authfail deny=5 unlock_time=1800" >> /etc/pam.d/system-auth
fi
