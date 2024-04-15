#README
#Introduction
#Welcome to the README file for configuring the firewall on web-01 using ufw. This document provides step-by-step instructions for fulfilling both mandatory and advanced tasks related to firewall setup and port forwarding.

#Sections
#Task 1: Mandatory - Blocking Incoming Traffic
#Task 2: Advanced - Port Forwarding
#Additional Notes
#Task 1: Mandatory - Blocking Incoming Traffic
#Requirements
Configure ufw to block all incoming traffic, except for specific TCP ports.
Ensure the following TCP ports are allowed:
22 (SSH)
443 (HTTPS SSL)
80 (HTTP)
#Steps
Install ufw firewall.
Configure ufw to allow traffic on specified TCP ports.
Enable the firewall.
#Task 2: Advanced - Port Forwarding
#Requirements
Configure port forwarding on web-01 to redirect traffic from port 8080/TCP to port 80/TCP.
#Steps
Modify the ufw configuration file to enable port forwarding.
Add a port forwarding rule to redirect traffic.
Reload ufw for changes to take effect.
#Additional Notes
Ensure that configurations are applied only to web-01 unless specified otherwise.
Verify changes using appropriate commands and testing methods.
Document any deviations or additional configurations made during setup.
