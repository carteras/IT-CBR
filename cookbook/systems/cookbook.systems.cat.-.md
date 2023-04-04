# The weirdness of cat -

## Learning Intentions

* Display the contents of a file named "-" to standard output using the cat command in Linux.
* Understand the special meaning of "-" in Linux filenames and why it can be problematic.

## Selection Criteria

* Successfully display the contents of a file named "-" to standard output using the cat command in Linux.
* Explain the special meaning of "-" in Linux filenames and why it can be problematic.

## Description

A file with the name "-" is special in Linux because it has a special meaning. This makes it difficult to work with, but this recipe will help you learn how to display its contents to standard output.

### What is Cat?

* `cat` is a command in Linux used to display the contents of a file in the terminal.

### Why `-` Can Be Problematic?

The `-` symbol has a special meaning in Linux, so it can be confusing to use it as a filename. In Linux, `-` is a reserved character used to represent standard input or output, depending on the context. When used as a filename, Linux interprets it as a command line option instead of a file name, leading to unexpected behaviours or error messages.

## Recipe

Open the terminal program on your computer.

Type the following command and press Enter:

```shell-session
cat "-"
```

This command will display the contents of the "-" file to standard output on your screen.

Note: If you receive an error message with the above command, try using "./-" instead of "-" as follows:

```shell-session
cat ./-
```

This should work for most cases where the filename is "-".