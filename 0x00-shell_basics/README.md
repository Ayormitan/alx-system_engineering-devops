**Shell Basics**

This repository contains a collection of scripts written in the Shell scripting language. The scripts are designed to perform various tasks related to file management and directory operations. They are all developed based on the following requirements:

**General Requirements**
Allowed editors: vi, vim, emacs
All scripts will be tested on Ubuntu 20.04 LTS
All scripts should be exactly two lines long ($ wc -l file should print 2)
All files should end with a new line
The first line of all files should be exactly #!/bin/bash
A README.md file at the root of the repository, containing a description of the repository
A README.md file at the root of the project folder, describing what each script does
The usage of backticks, &&, ||, or ; is not allowed
All scripts must be executable. To make your file executable, use the chmod command: chmod u+x file
Scripts

**Print Absolute Path:** This script prints the absolute path name of the current working directory.

**Display Contents List:** This script displays the contents list of the current directory.

**Change to Home Directory:** This script changes the working directory to the user's home directory.

Display Current Directory Contents (Long Format): This script displays the contents of the current directory in a long format, including user and group IDs displayed numerically.

Display Current Directory Contents (Including Hidden Files): This script displays the contents of the current directory, including hidden files starting with .. It uses the long format.

Display Current Directory Contents: This script displays the contents of the current directory.

Create Directory: This script creates a directory named my_first_directory in the /tmp/ directory.

Move File: This script moves the file betty from /tmp/ to /tmp/my_first_directory.

Delete File: This script deletes the file betty.

Delete Directory: This script deletes the directory my_first_directory in the /tmp directory.

Change to Previous Directory: This script changes the working directory to the previous one.

List Files: This script lists all files in the current directory, the parent of the working directory, and the /boot directory (in this order) in a long format. It includes hidden files starting with ..

Print File Type: This script prints the type of the file named iamafile. The file iamafile will be located in the /tmp directory when the script is executed.

Create Symbolic Link: This script creates a symbolic link named __ls__ to /bin/ls in the current working directory.

Copy HTML Files: This script copies all HTML files from the current working directory to the parent of the working directory. It only copies files that do not exist in the parent directory or are newer than the versions in the parent directory. The HTML files have the extension .html.

Please ensure that you have the necessary permissions to execute the scripts. For any additional information about each script, refer to the respective README.md file in the project folder.

Note: This README file is a general overview of the repository and does not provide detailed implementation instructions for each script.
