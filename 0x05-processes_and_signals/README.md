# Processes and Signals

## Resources
- [Linux PID](https://linux.die.net/man/5/proc)
- [Linux process](https://linux.die.net/man/1/ps)
- [Linux signal](https://linux.die.net/man/7/signal)
- [Process management in Linux](https://www.geeksforgeeks.org/operating-system-process-management/)

## Author
Omotayo Ayomitan

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks

### Task 1
Write a Bash script that displays its own PID.

### Task 2
Write a Bash script that displays a list of currently running processes.
#### Requirements:
- Must show all processes, for all users, including those which might not have a TTY
- Display in a user-oriented format
- Show process hierarchy

### Task 3
Write a Bash script that displays lines containing the `bash` word, thus allowing you to easily get the PID of your Bash process.
#### Requirements:
- You cannot use `pgrep`
- The third line of your script must be `# shellcheck disable=SC2009`

### Task 4
Write a Bash script that displays the PID, along with the process name, of processes whose name contains the word `bash`.
#### Requirements:
- You cannot use `ps`

### Task 5
Write a Bash script that displays "To infinity and beyond" indefinitely.
#### Requirements:
- In between each iteration of the loop, add a `sleep 2`

### Task 6
Write a Bash script that stops the `4-to_infinity_and_beyond` process.
#### Requirements:
- You must use `kill`

### Task 7
Write a Bash script that stops the `4-to_infinity_and_beyond` process.
#### Requirements:
- You cannot use `kill` or `killall`

### Terminal #0

### Task 8
Write a Bash script that displays:
- "To infinity and beyond" indefinitely
- With a `sleep 2` in between each iteration
- "I am invincible!!!" when receiving a `SIGTERM` signal
- Make a copy of your `6-stop_me_if_you_can` script, name it `67-stop_me_if_you_can`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond` one.

### Task 9
Write a Bash script that kills the process `7-highlander`.

