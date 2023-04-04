# How do you handle spaces in files?

## Learning Intentions

* Teach students how to properly handle file names with spaces in Linux
* Introduce students to two methods of executing a `cat` command on a file with spaces in its name - using quotes and tab completion
* Enable students to effectively navigate to the correct directory, execute the `cat` command with a file name containing spaces, and view the contents of the file in the terminal window.

## Selection Criteria

* You will be able to open or `cat` files that have spaces in their names. 

## Description

You will encounter files that have spaces in their names. How do you open them? 

## Recipe

1. Open the terminal and navigate to the directory where the file is located using the `cd` command.

2. Open the terminal and navigate to the starting position using the command `cd ~/Documents/git/networking_security_cyber_security_challenge`.

3. Navigate to the directory challenge2 using the command `cd challenge2`.

4. Type `cat` followed by a space.

5. Type the file name, including the spaces, and wrap the entire name in quotes. For example:

```shell
cat "how do you handle files with spaces in them"
```

6. Press enter to execute the command.

7. The contents of the file should now be displayed in the terminal window.

Alternatively, you can also use tab completion as follows:

1. Open the terminal and navigate to the starting position using the command `cd ~/Documents/git/networking_security_cyber_security_challenge`.

2. Navigate to the directory challenge2 using the command `cd challenge2`.

3. Type cat followed by a space.

4. Type the first few characters of the file name, "how", then press the tab key. This will automatically complete the file name, adding a backslash before each space.

```shell
cat how[TAB] 
cat how\ do\ you\ handle\ files\ with\ spaces\ in\ them
```

5. Press enter to execute the command.

The contents of the file should now be displayed in the terminal window.
