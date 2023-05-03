# Introduction to SSH

SSH (Secure Shell) is a cryptographic network protocol that enables secure communication between computers over an unsecured network. It is commonly used to access remote servers, transfer files, and execute remote commands. SSH provides strong encryption and authentication, ensuring that data transmitted over the network remains confidential and protected from unauthorized access.

## Using SSH to Connect to a Remote Server

In this tutorial, we will use the ssh command to connect to a remote computer with the following credentials:

```
Hostname: bushranger0@10.13.37.152
Port: 22
Password: bushranger0
```

Note: For CTF (Capture The Flag) challenges, the hostname, port, and password will be different. Ensure you use the provided credentials for your specific challenge.

## Steps to Connect Using SSH

Open a terminal (Linux or macOS) or use an SSH client like PuTTY (Windows).

Type the following command to establish a connection to the remote server:

```shell
ssh bushranger0@10.13.37.152 -p 22
```

* ssh: This is the command to initiate an SSH connection.
* bushranger0@10.13.37.152: This specifies the user (bushranger0) and the server's IP address (10.13.37.152).
* -p 22: This specifies the port number (22) for the SSH connection.
* If this is your first time connecting to the server, you will see a message asking if you want to trust the remote host. Type yes and press Enter to continue.

You will be prompted for the password. Enter the password bushranger0 and press Enter. Note that the password will not be displayed as you type.

If the credentials are correct, you will be connected to the remote server, and you can start running commands on the remote machine.

To disconnect from the remote server, simply type exit and press Enter.