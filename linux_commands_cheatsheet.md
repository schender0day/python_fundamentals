# Linux Commands Cheat Sheet (From Basic to Advanced)
In this Linux cheat sheet, we cover the most essential Linux commands, ranging from basic to advanced. Both beginners and experienced professionals can benefit from this resource.

## 1. File and Directory Operations Commands
File and directory operations are fundamental when working with the Linux OS. Below are some commonly used commands for these operations:

| Command | Description | Options | Examples |
|---------|-------------|---------|----------|
| `ls`    | List files and directories. | `-l`: Long format listing.<br>`-a`: Include hidden files.<br>`-h`: Human-readable file sizes. | `ls -l`: Displays files and directories with details.<br>`ls -a`: Shows all files and directories, including hidden ones.<br>`ls -lh`: Displays file sizes in a human-readable format. |
| `cd`    | Change directory. | | `cd /path/to/directory`: Changes the current directory to the specified path. |
| `pwd`   | Print current working directory. | | `pwd`: Displays the current directory. |
| `mkdir` | Create a new directory. | | `mkdir my_directory`: Creates a new directory named "my_directory". |
| `rm`    | Remove files and directories. | `-r`: Remove directories recursively.<br>`-f`: Force removal without confirmation. | `rm file.txt`: Deletes "file.txt".<br>`rm -r my_directory`: Deletes "my_directory" and its contents.<br>`rm -f file.txt`: Forcefully deletes "file.txt" without confirmation. |
| `cp`    | Copy files and directories. | `-r`: Copy directories recursively. | `cp -r directory destination`: Copies the directory and its contents to the destination.<br>`cp file.txt destination`: Copies "file.txt" to the destination. |
| `mv`    | Move/rename files and directories. | | `mv file.txt new_name.txt`: Renames "file.txt" to "new_name.txt".<br>`mv file.txt directory`: Moves "file.txt" to the specified directory. |
| `touch` | Create an empty file or update file timestamps. | | `touch file.txt`: Creates an empty file named "file.txt". |
| `cat`   | View the contents of a file. | | `cat file.txt`: Displays the contents of "file.txt". |
| `head`  | Display the first few lines of a file. | `-n`: Specify the number of lines to display. | `head file.txt`: Shows the first 10 lines of "file.txt".<br>`head -n 5 file.txt`: Displays the first 5 lines of "file.txt". |
| `tail`  | Display the last few lines of a file. | `-n`: Specify the number of lines to display. | `tail file.txt`: Shows the last 10 lines of "file.txt".<br>`tail -n 5 file.txt`: Displays the last 5 lines of "file.txt". |
| `ln`    | Create links between files. | `-s`: Create symbolic (soft) links. | `ln -s source_file link_name`: Creates a symbolic link named "link_name" pointing to "source_file". |
| `find`  | Search for files and directories. | `-name`: Search by filename.<br>`-type`: Search by file type. | `find /path/to/search -name "*.txt"`: Searches for all files with ".txt" extension in the specified directory. |

## 2. File Permission Commands
File permissions in Linux and Unix control access to files and directories. The three basic permissions are read, write, and execute. Each permission can be granted or denied to three user categories: the file's owner, the file's group members, and everyone else.

| Command | Description | Options | Examples |
|---------|-------------|---------|----------|
| `chmod` | Change file permissions. | `u`: User/owner permissions.<br>`g`: Group permissions.<br>`o`: Other permissions.<br>`+`: Add permissions.<br>`-`: Remove permissions.<br>`=`: Set permissions explicitly. | `chmod u+rwx file.txt`: Grants read, write, and execute permissions to the file's owner. |
| `chown` | Change file ownership. | | `chown user file.txt`: Changes the owner of "file.txt" to the specified user. |
| `chgrp` | Change group ownership. | | `chgrp group file.txt`: Changes the group ownership of "file.txt" to the specified group. |
| `umask` | Set default file permissions. | | `umask 022`: Sets the default file permissions to read and write for the owner, and read-only for the group and others. |

## 3. File Compression and Archiving Commands
Here are commands for file compression and archiving in Linux:

| Command | Description | Options | Examples |
|---------|-------------|---------|----------|
| `tar`   | Create or extract archive files. | `-c`: Create a new archive.<br>`-x`: Extract files from an archive.<br>`-f`: Specify the archive filename.<br>`-v`: Verbose mode.<br>`-z`: Compress the archive with gzip.<br>`-j`: Compress the archive with bzip2. | `tar -czvf archive.tar.gz files/`: Creates a compressed tar archive named "archive.tar.gz" containing files from the "files/" directory. |
| `gzip`  | Compress files. | `-d`: Decompress files. | `gzip file.txt`: Compresses "file.txt" and renames it as "file.txt.gz". |
| `zip`   | Create compressed zip archives. | `-r`: Recursively include directories. | `zip archive.zip file1.txt file2.txt`: Creates a zip archive named "archive.zip" containing "file1.txt" and "file2.txt". |

## 4. Process Management Commands
Process management commands in Linux allow you to monitor and control running processes on the system. Here are some of the most commonly used process management commands:

| Command | Description | Options | Examples |
|---------|-------------|---------|----------|
| `ps`    | Display running processes. | `-aux`: Show all processes. | `ps aux`: Shows all running processes with detailed information. |
| `top`   | Monitor system processes in real-time. | | `top`: Displays a dynamic view of system processes and resource usage. |
| `kill`  | Terminate a process. | `-9`: Forcefully kill a process. | `kill PID`: Terminates the process with the specified process ID. |
| `pkill` | Terminate processes based on their name. | | `pkill process_name`: Terminates all processes with the specified name. |
| `pgrep` | List processes based on their name. | | `pgrep process_name`: Lists all processes with the specified name. |

## 5. System Information Commands
There are several commands in Linux to gather system information. Here are some of the most commonly used system information commands:

| Command  | Description | Options | Examples |
|----------|-------------|---------|----------|
| `uname`  | Print system information. | `-a`: All system information. | `uname -a`: Displays all system information. |
| `whoami` | Display current username. | | `whoami`: Shows the current username. |
| `df`     | Show disk space usage. | `-h`: Human-readable sizes. | `df -h`: Displays disk space usage in a human-readable format. |
| `du`     | Estimate file and directory sizes. | `-h`: Human-readable sizes.<br>`-s`: Display total size only. | `du -sh directory/`: Provides the total size of the specified directory. |
| `free`   | Display memory usage information. | `-h`: Human-readable sizes. | `free -h`: Displays memory usage in a human-readable format. |
| `uptime` | Show system uptime. | | `uptime`: Shows the current system uptime. |
| `lscpu`  | Display CPU information. | | `lscpu`: Provides detailed CPU information. |

## 6. Networking Commands
There are several networking commands in Linux to manage and troubleshoot network connections. Here are some of the most commonly used networking commands:

| Command  | Description | Examples |
|----------|-------------|----------|
| `ifconfig` | Display network interface information. | `ifconfig`: Shows details of all network interfaces. |
| `ping`     | Send ICMP echo requests to a host. | `ping google.com`: Sends ICMP echo requests to "google.com" to check connectivity. |
| `netstat`  | Display network connections and statistics. | `netstat -tuln`: Shows all listening TCP and UDP connections. |
| `ss`       | Display network socket information. | `ss -tuln`: Shows all listening TCP and UDP connections. |
| `ssh`      | Securely connect to a remote server. | `ssh user@hostname`: Initiates an SSH connection to the specified hostname. |
| `scp`      | Securely copy files between hosts. | `scp file.txt user@hostname:/path/to/destination`: Securely copies "file.txt" to the specified remote host. |
| `wget`     | Download files from the web. | `wget http://example.com/file.txt`: Downloads "file.txt" from the specified URL. |
| `curl`     | Transfer data to or from a server. | `curl http://example.com`: Retrieves the content of a webpage from the specified URL. |

## 7. IO Redirection Commands
IO (Input/Output) redirection commands in Linux are used to redirect the standard input, output, and error streams of commands and processes. Here are some of the most commonly used IO redirection commands:

| Command | Description |
|---------|-------------|
| `cmd < file` | Input of cmd is taken from the file. |
| `cmd > file` | Standard output (stdout) of cmd is redirected to the file. |
| `cmd 2> file` | Error output (stderr) of cmd is redirected to the file. |
| `cmd 2>&1` | stderr is redirected to the same place as stdout. |
| `cmd1 <(cmd2)` | Output of cmd2 is used as the input file for cmd1. |
| `cmd > /dev/null` | Discards the stdout of cmd by sending it to the null device. |
| `cmd &> file` | Every output of cmd is redirected to the file. |
| `cmd 1>&2` | stdout is redirected to the same place as stderr. |
| `cmd >> file` | Appends the stdout of cmd to the file. |

## 8. Environment Variable Commands
In Linux, environment variables store configuration settings, system information, and other variables that can be accessed by processes and shell scripts. Here are some of the most commonly used environment variable commands:

| Command | Description |
|---------|-------------|
| `export VARIABLE_NAME=value` | Sets the value of an environment variable. |
| `echo $VARIABLE_NAME` | Displays the value of a specific environment variable. |
| `env` | Lists all environment variables currently set in the system. |
| `unset VARIABLE_NAME` | Unsets or removes an environment variable. |
| `export -p` | Shows a list of all currently exported environment variables. |
| `env VAR1=value COMMAND` | Sets the value of an environment variable for a specific command. |
| `printenv` | Displays the values of all environment variables. |

## 9. User Management Commands
User management commands in Linux allow you to create, modify, and manage user accounts on the system. Here are some of the most commonly used user management commands:

| Command | Description |
|---------|-------------|
| `who` | Show who is currently logged in. |
| `sudo adduser username` | Create a new user account on the system with the specified username. |
| `finger` | Display information about all users currently logged into the system, including their usernames, login times, and terminals. |
| `sudo deluser USER GROUPNAME` | Remove the specified user from the specified group. |
| `last` | Show recent login history of users. |
| `finger username` | Provide information about the specified user, including their username, real name, terminal, idle time, and login time. |
| `sudo userdel -r username` | Delete the specified user account from the system, including their home directory and associated files. The `-r` option ensures the removal of the user's files. |
| `sudo passwd -l username` | Lock the password of the specified user account, preventing the user from logging in. |
| `su – username` | Switch to another user account with the user's environment. |
| `sudo usermod -a -G GROUPNAME USERNAME` | Add an existing user to the specified group. The user is added to the group without removing them from their current groups. |

## 10. Shortcuts Commands
There are numerous shortcut commands in Linux that can enhance your productivity. Here are a few of the most common ones:

### 10.1: Bash Shortcuts Commands:
| Navigation | Description | Editing | Description | History | Description |
|------------|-------------|---------|-------------|---------|-------------|
| `Ctrl + A` | Move to the beginning of the line. | `Ctrl + U` | Cut/delete from the cursor position to the beginning of the line. | `Ctrl + R` | Search command history (reverse search). |
| `Ctrl + E` | Move to the end of the line. | `Ctrl + K` | Cut/delete from the cursor position to the end of the line. | `Ctrl + G` | Escape from history search mode. |
| `Ctrl + B` | Move back one character. | `Ctrl + W` | Cut/delete the word before the cursor. | `Ctrl + P` | Go to the previous command in history. |
| `Ctrl + F` | Move forward one character. | `Ctrl + Y` | Paste the last cut text. | `Ctrl + N` | Go to the next command in history. |
| `Alt + B` | Move back one word. | `Ctrl + L` | Clear the screen. | `Ctrl + C` | Terminate the current command. |
| `Alt + F` | Move forward one word. | | | | |

### 10.2: Nano Shortcuts Commands:
| File Operations | Description | Navigation | Description | Editing | Description | Search and Replace | Description |
|-----------------|-------------|------------|-------------|---------|-------------|--------------------|-------------|
| `Ctrl + O` | Save the file. | `Ctrl + Y` | Scroll up one page. | `Ctrl + K` | Cut/delete from the cursor position to the end of the line. | `Ctrl + W` | Search for a string in the text. |
| `Ctrl + X` | Exit Nano (prompt to save if modified). | `Ctrl + V` | Scroll down one page. | `Ctrl + U` | Uncut/restore the last cut text. | `Alt + W` | Search and replace a string in the text. |
| `Ctrl + R` | Read a file into the current buffer. | `Alt + \` | Go to a specific line number. | `Ctrl + 6` | Mark a block of text for copying or cutting. | `Alt + R` | Repeat the last search. |
| `Ctrl + J` | Justify the current paragraph. | `Alt + ,` | Go to the beginning of the current line. | `Ctrl + K` | Cut/delete the marked block of text. | | |
| | | `Alt + .` | Go to the end of the current line. | `Alt + 6` | Copy the marked block of text. | | |

### 10.3: VI Shortcuts Commands:
| Command | Description |
|---------|-------------|
| `cw` | Change the current word. Deletes from the cursor position to the end of the current word and switches to insert mode. |
| `dd` | Delete the current line. |
| `x` | Delete the character under the cursor. |
| `R` | Enter replace mode. Overwrites characters starting from the cursor position until you press the Escape key. |
| `o` | Insert a new line below the current line and switch to insert mode. |
| `u` | Undo the last change. |
| `s` | Substitute the character under the cursor and switch to insert mode. |
| `dw` | Delete from the cursor position to the beginning of the next word. |
| `D` | Delete from the cursor position to the end of the line. |
| `4dw` | Delete the next four words from the cursor position. |
| `A` | Switch to insert mode at the end of the current line. |
| `S` | Delete the current line and switch to insert mode. |
| `r` | Replace the character under the cursor with a new character entered from the keyboard. |
| `i` | Switch to insert mode before the cursor. |
| `3dd` | Delete the current line and the two lines below it. |
| `ESC` | Exit from insert or command-line mode and return to command mode. |
| `U` | Restore the current line to its original state before any changes were made. |
| `~` | Switch the case of the character under the cursor. |
| `a` | Switch to insert mode after the cursor. |
| `C` | Delete from the cursor position to the end of the line and switch to insert mode. |

### 10.4: Vim Shortcuts Commands:
| Normal Mode | Description | Command Mode | Description | Visual Mode | Description |
|-------------|-------------|--------------|-------------|-------------|-------------|
| `i` | Enter insert mode at the current cursor position. | `:w` | Save the file. | `v` | Enter visual mode to select text. |
| `x` | Delete the character under the cursor. | `:q` | Quit Vim. | `y` | Copy the selected text. |
| `dd` | Delete the current line. | `:q!` | Quit Vim without saving changes. | `d` | Delete the selected text. |
| `yy` | Copy the current line. | `:wq` or `😡` | Save and quit Vim. | `p` | Paste the copied or deleted text. |
| `p` | Paste the copied or deleted text below the current line. | `:s/old/new/g` | Replace all occurrences of "old" with "new" in the file. | | |
| `u` | Undo the last change. | `:set nu` or `:set number` | Display line numbers. | | |
| `Ctrl + R` | Redo the last undo. | | | | |

## Conclusion
Linux is a widely used operating system for development. As a developer, it's essential to know Linux basics and commands. This Cheat Sheet covers commands for directory creation, file compression, archiving, process management, system information, networking, and more. It's organized and categorized for quick access to commands for specific use cases. Using this resource can enhance your productivity and improve your understanding of the Linux operating system.

