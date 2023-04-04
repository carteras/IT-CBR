# How to Use the Linux file Command to Check if Files are Human-Readable

The file command is a tool used in Linux and other Unix-like operating systems to identify the type of a file. It can also determine if a file is human-readable (ASCII). In this guide, you will learn how to use the file command to check if files are human-readable.

## Background Information

ASCII is a character encoding that uses 7 bits to represent each character. This encoding is commonly used for plain text files, which are human-readable. In contrast, there are other file types that may not be human-readable, such as binary files, which contain non-textual data.

## Steps to Check if Files are Human-Readable

* Open your terminal application.
* Navigate to the directory that contains the file you want to check.
* Type file followed by the name of the file, and press Enter. For example, if the file is named "example.txt", you would type file example.txt.
* The file command will display information about the file, including its type. If the file is human-readable (ASCII), the type will be displayed as "ASCII text". If the file is not human-readable, the type will be displayed as "data".

### Other Common Tasks with file Command

* Determining the file type of an unknown file.
* Checking the endianness of a binary file.
* Displaying the contents of a compressed file without decompressing it.
* Identifying the encoding of a text file.
* Checking the integrity of a downloaded file.

### Hint for Using the man Command

If you're not sure how to use the file command to determine the type of an unknown file, you can use the man command to access the manual page for the file command. To access the manual page, type man file and press Enter. This will display the manual page for the file command, which includes information on how to use the command to determine the type of an unknown file.