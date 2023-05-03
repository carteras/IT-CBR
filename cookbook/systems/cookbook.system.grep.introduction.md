# Title: Summary of grep Command with Example

grep is a powerful command-line utility in Linux for searching text files and displaying lines that match a specified pattern. The basic syntax of grep is:

```shell
grep <pattern> <file>
```

<pattern>: The search pattern or regular expression.
<file>: The file to search.

## Example 1: Using grep to Find a Specific Pattern in a Long Text File

Suppose you have a long text file called example.txt and you want to find all the lines containing the word "Linux":

```shell
grep "Linux" example.txt
```
The command will display all lines in the example.txt file that contain the word "Linux".

## Example 2 piping grep to search the output of another program

Using grep with pipes allows you to search for patterns within the output of another command. In this example, we will use ls to list files in a directory and then pipe the output to grep to filter the results:

```shell
ls | grep "foo"
```

This command will list all files in the current directory and display only those containing the word "foo" in their filenames.

In summary, grep is a versatile command for searching text files based on patterns or regular expressions. Use it to find specific content within files, filter output, or parse logs more efficiently.
