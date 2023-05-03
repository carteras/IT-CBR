# Title: Summary of sort Command with Example

sort is a command-line utility in Linux used for sorting lines of text files. The basic syntax of sort is:

```shell
sort <file>
```

<file>: The file to sort.

By default, sort orders lines in alphabetical order, treating each line as a single field. You can also sort numerically, reverse the order, and sort based on specific fields.

## Example: Using sort to Sort a List of Numbers

Suppose you have a file called numbers.txt containing the following numbers:

```
5
3
10
1
8
```

To sort the numbers in ascending order, use the sort command with the -n option for numeric sorting:

```shell
sort -n numbers.txt
```

The output will display the sorted numbers:

```
1
3
5
8
10
```

In summary, the sort command is a useful tool for sorting text files based on various criteria. It is versatile and can handle different data types, making it an essential command for organizing and analyzing data in Linux.
