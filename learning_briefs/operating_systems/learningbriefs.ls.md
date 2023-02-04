# ls 

The `ls` command in Linux is short for "list", and is used to list the files and directories in a directory. It displays the names of files and directories in the current working directory, or in a specified directory if a directory is provided as an argument to the command. The `ls` command is one of the most commonly used commands in Linux, and has many options for customizing the output display.

## Learning Goals

*By the end of this module you should be able to answer the following:*

* Understanding the basic syntax and options of the ls command, such as ls -l or ls -a.
* Being able to list the files and directories in a directory, and distinguish between the two.
* Understanding the different columns of information displayed in the ls -l output, such as permissions, owner, group, size, and date/time of modification.
* Knowing how to sort the output of the ls command based on various criteria, such as size, date/time, or alphabetically.
* Being able to use wildcard characters, such as * or ?, to match patterns of files or directories in the output.
* Knowing how to combine multiple options to customize the output of the ls command to meet specific needs.

## Commands

*It is important to practice commands and challenge our brain in new ways. Do all of the problems below, including the example problems. They will make you a better operator.*


### basic syntax of the ls command 

The basic syntax of the `ls` command is simply `ls`. This will list the files and directories in the current working directory. To list the contents of a specific directory, you can specify the directory path after the `ls` command, for example: `ls /path/to/directory`.

Options can also be added to the ls command to modify its behaviour, for example: `ls -l` or `ls -a`. The options are preceded by a hyphen (-) and can be combined to produce a desired result.

### How to list all the files in a directory

To list all of the files in a directory using the ls command, use the option -a to show hidden files, which are normally hidden from view:

```bash
ls -a
```

This will show all files, including hidden files (files that start with a dot .), in the current directory. If you want to list the files in a specific directory, you can specify the directory path after the ls command, for example:

```bash
ls -a /path/to/directory
```


## Practice Questions


### Practice:

## Fluff about find out

So, you've learnt lots of things so far today. I challenge you to use your imagination and try and find some things that you feel you might be able to do, but weren't necessarily taught.

Because it's our first week, I am happy to give you some hints to start you off, but go nuts. 


## Bug hunt

Kevin has written some code and it doesn't work. What's wrong with it?
