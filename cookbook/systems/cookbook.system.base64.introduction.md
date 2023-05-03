# Title: Summary of base64 Command with Examples

base64 is a command-line utility in Linux used for encoding and decoding data using the Base64 encoding scheme. The basic syntax of base64 is:

```shell
base64 [OPTION] [FILE]
```

[OPTION]: The options to use, such as -d for decoding.
[FILE]: The file to process. If omitted, base64 reads from standard input.

## Understanding Base64

Base64 is an encoding scheme that represents binary data in an ASCII string format. It is commonly used for encoding data when there is a need to transfer it over media that is designed to deal with textual data, such as email or web forms. Base64 is not an encryption method; it is simply a way to represent binary data in a text format.

## Example 1: Encoding Data with base64

Suppose you have a file called data.txt containing the following text:

```
Hello, World!
```

To encode the data in Base64 format, use the base64 command:

```shell
base64 data.txt
```

The output will display the encoded data:

```makefile
SGVsbG8sIFdvcmxkIQ==
```

## Example 2: Decoding Base64 Data

To decode the previously encoded Base64 data, use the base64 command with the -d option:

```shell
echo "SGVsbG8sIFdvcmxkIQ==" | base64 -d
```

The output will display the original data:

```
Hello, World!
```

In summary, the base64 command is a useful tool for encoding and decoding data using the Base64 encoding scheme. It enables you to represent binary data in a text format, making it suitable for transmission over media designed for textual data.
