#!/bin/bash
# adjust_password_complexity_policy.sh
# Set password complexity policy on Ubuntu 20.04 and CentOS 7

# Ubuntu 20.04
if [[ -e /etc/pam.d/common-password ]]; then
    echo "Setting password policy on Ubuntu..."
    sed -i '/pam_pwquality.so/ s/^#//' /etc/pam.d/common-password
    sed -i '/pam_pwquality.so/ s/try_first_pass retry=3/try_first_pass retry=3 minlen=12 dcredit=-1 ucredit=-1 ocredit=-1 lcredit=-1/' /etc/pam.d/common-password
fi

# CentOS 7
if [[ -e /etc/security/pwquality.conf ]]; then
    echo "Setting password policy on CentOS..."
    sed -i '/minlen/ s/9/12/' /etc/security/pwquality.conf
    sed -i '/dcredit/ s/-1/-1/' /etc/security/pwquality.conf
    sed -i '/ucredit/ s/-1/-1/' /etc/security/pwquality.conf
    sed -i '/ocredit/ s/-1/-1/' /etc/security/pwquality.conf
    sed -i '/lcredit/ s/-1/-1/' /etc/security/pwquality.conf
fi
