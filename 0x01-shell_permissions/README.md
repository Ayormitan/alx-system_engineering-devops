0x01. Shell, permissions, Requirements
This repository contains shell scripts that demonstrate various operations related to shell commands and permissions. The scripts are specifically designed for Ubuntu 20.04 LTS and should be exactly two lines long. Each file ends with a new line and starts with #!/bin/bash as the first line. This README.md file provides an overview of each script's functionality.

Scripts
1-switch_user_to_betty.sh
This script switches the current user to the user betty.

2-effective_username.sh
This script prints the effective username of the current user.

3-groups_of_current_user.sh
This script prints all the groups the current user is a part of.

4-change_owner_to_betty.sh
This script changes the owner of the file hello to the user betty.

5-create_empty_file_hello.sh
This script creates an empty file called hello.

6-add_execute_permission_to_owner_hello.sh
This script adds execute permission to the owner of the file hello.

7-add_execute_permission_to_owner_and_group_hello.sh
This script adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

8-add_execute_permission_to_all_hello.sh
This script adds execution permission to the owner, the group owner, and other users, to the file hello.

9-set_permissions_to_file_hello.sh
This script sets the permission to the file hello as follows:

Owner: no permission at all
Group: no permission at all
Other users: all permissions
10-set_mode_of_file_hello.sh
This script sets the mode of the file hello to -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello.

11-set_mode_of_file_hello_same_as_olleh.sh
This script sets the mode of the file hello the same as the mode of the file olleh.

12-add_execute_permission_to_subdirectories.sh
This script adds execute permission to all subdirectories of the current directory for the owner, the group owner, and all other users. Regular files should not be changed.

13-create_directory_my_dir.sh
This script creates a directory called my_dir with permissions 751 in the working directory.

14-change_group_owner_to_school.sh
This script changes the group owner of the file hello to school.
