# Shell, I/O Redirections, and Filters

This project consists of several shell scripts that demonstrate various concepts related to Shell, I/O Redirections, and Filters.

## Requirements

- Allowed editors: vi, vim, emacs
- All scripts will be tested on Ubuntu 20.04 LTS
- All scripts should be exactly two lines long (`$ wc -l file` should print 2)
- All files should end with a new line
- The first line of all files should be exactly `#!/bin/bash`
- A README.md file, at the root of the project folder, describing what each script does
- You are not allowed to use backticks, `&&`, `||`, or `;`
- All files must be executable
- You are not allowed to use `sed` or `awk`

## Scripts

### 0. Hello World

- File: `0-hello_world`
- Description: This script prints "Hello, World" followed by a new line to the standard output.

### 1. Confused Smiley

- File: `1-confused_smiley`
- Description: This script displays a confused smiley "(Ôo)'.

### 2. Display /etc/passwd

- File: `2-display_passwd`
- Description: This script displays the content of the `/etc/passwd` file.

### 3. Display /etc/passwd and /etc/hosts

- File: `3-display_passwd_hosts`
- Description: This script displays the content of the `/etc/passwd` and `/etc/hosts` files.

### 4. Display last 10 lines of /etc/passwd

- File: `4-display_last_lines`
- Description: This script displays the last 10 lines of the `/etc/passwd` file.

### 5. Display first 10 lines of /etc/passwd

- File: `5-display_first_lines`
- Description: This script displays the first 10 lines of the `/etc/passwd` file.

### 6. Display third line of the file iacta

- File: `6-third_line`
- Description: This script displays the third line of the file `iacta` which is located in the working directory.

### 7. Create a file with special characters

- File: `7-file_with_special_characters`
- Description: This script creates a file named exactly `*\\'"Best School"'\\*$?*****:)` containing the text "Best School" ending with a new line.

### 8. Write ls -la output to a file

- File: `8-ls_cwd_content`
- Description: This script writes the result of the command `ls -la` into the file `ls_cwd_content`. If the file already exists, it will be overwritten. If the file does not exist, it will be created.

### 9. Duplicate the last line of iacta

- File: `9-duplicate_last_line`
- Description: This script duplicates the last line of the file `iacta` located in the working directory.

### 10. Delete .js files

- File: `10-delete_js_files`
- Description: This script deletes all regular files (not directories) with a `.js` extension in the current directory and its subfolders.

### 11. Count directories and sub-directories

- File: `11-count_directories`
- Description: This script counts the number of directories and sub-directories in the current directory. The current and parent directories are not taken into account, and hidden directories are included in the count.

### 12. Display the 10 newest files

- File: `12-newest_files`
- Description: This script displays the 10 newest files in the current directory.

