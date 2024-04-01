#!/usr/bin/env bash
#Using puppet to make a change in configuration file

file { 'etc/ssh/ssh_config':
	ensure => present,
content =>"
	#SSH client configuration
	host*
	IdentifyFile ~/.ssh/school
	PasswordAuthentication no"
}
