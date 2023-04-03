# Using GIT

This cookbook recipe will guide you through the process of using Git to clone the networking_security_cyber_security_challenges repository from GitHub and how to update that repository on Manjaro Linux.

Git is a version control system that allows you to keep track of changes to your code over time. It is commonly used for collaborative software development and is essential for working with GitHub repositories.

For the purposes of this recipe, we will use the example from the Networking and Cyber Security unit challenge. 

To clone the networking_security_cyber_security_challenges repository from GitHub on Manjaro Linux, you can follow these steps:

1. Open a terminal window by pressing `meta` on your keyboard and typing `konsole` or clicking the konsole icon in your task bar.
2. Navigate to the directory where you want to clone the repository by typing `cd ~/Documents/git/` and pressing Enter. This will take you to the git directory within your Documents directory. You can create the `git` directory if it doesn't exist by typing `mkdir -p ~/Documents/git/` and pressing Enter.
3. In the terminal window, type `git clone https://github.com/carteras/networking_security_cyber_security_challenges.git` and press Enter. This will create a local copy of the repository in your current directory.

To update your local repository with changes made on the remote repository, you can follow these steps:

1. Open a terminal window and navigate to the local repository directory by typing cd ~/Documents/git/networking_security_cyber_security_challenges and pressing Enter. This will take you to the cloned repository directory.
2. Type git pull and press Enter. This will fetch any changes made to the remote repository and merge them with your local repository.

To get started with basic command line navigation and file manipulation in Linux, you can refer to the following resources:

[Linux Command Line Basics](https://hackr.io/blog/basic-linux-commands)
[Linux Cheat Sheet](https://cheatography.com/davechild/cheat-sheets/linux-command-line/)