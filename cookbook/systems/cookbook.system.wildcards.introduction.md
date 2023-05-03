# Introduction to Wildcards

Wildcards are special characters used in Linux command line to represent one or more characters in a filename or pathname. They allow you to perform operations on multiple files simultaneously, based on patterns.

## The most common wildcards are:

* *: Represents any sequence of characters (including no characters at all).
* ?: Represents any single character.

## Using Wildcards with the file Command

Wildcards can be used with the file command to identify the type of multiple files simultaneously. To do so, use the * wildcard in place of the filename.

### Example 1 using the * wildcard

Suppose you have a directory with the following files:

```shell
file1.txt  file2.pdf  file3.png
```

To determine the type of all files in the directory, use the * wildcard with the file command:

```shell
file *
```

The output will display the file type for each file:

```shell
file1.txt: ASCII text
file2.pdf: PDF document, version 1.5
file3.png: PNG image data, 800 x 600, 8-bit/color RGBA, non-interlaced
```

### Example 2: Using the ? Wildcard

Suppose you have a directory with the following files:

```shell
fileA.txt  fileB.txt  file1.txt  file2.txt
```

To determine the type of all files starting with "file" followed by a single character and ending with ".txt", use the ? wildcard with the file command:

```shell
file file?.txt
```

The output will display the file type for the matching files:

```shell
fileA.txt: ASCII text
fileB.txt: ASCII text
```

Note: The file1.txt and file2.txt files were not included in the output because the ? wildcard only matches a single character.

Conclusion
Wildcards like * and ? are powerful tools in the Linux command line for working with multiple files simultaneously based on patterns. Use wildcards with commands like file to perform operations on a group of files at once.