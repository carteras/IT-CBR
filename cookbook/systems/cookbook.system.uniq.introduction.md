# Title: Summary of uniq Command with Examples

uniq is a command-line utility in Linux used for filtering out duplicate lines in a sorted text file. The basic syntax of uniq is:

```shell
uniq <file>
```

<file>: The sorted file to process.

By default, uniq removes adjacent duplicate lines, leaving only unique lines. It can also display only the duplicate or unique lines, and count the occurrences of each line.

## Example 1: Basic Usage of uniq

Suppose you have a sorted file called names.txt containing the following names:

```
Alice
Alice
Bob
Charlie
Charlie
Charlie
```

To remove adjacent duplicate lines, use the uniq command:

```shell
uniq names.txt
```
The output will display the unique names:

```
Alice
Bob
Charlie
```

## Example 2: Combining sort and uniq

Suppose you have an unsorted file called fruits.txt containing the following fruits:

```mathematica
Apple
Banana
Apple
Orange
Banana
```

To remove duplicates, first sort the file using the sort command, then pipe the output to uniq:

```shell
sort fruits.txt | uniq
```

The output will display the sorted unique fruits:

```mathematica
Apple
Banana
Orange
```


## Example 3: finding unique lines 

The -u option with uniq displays only the unique lines that are not duplicated. Here's an example using uniq -u:

Suppose you have a sorted file called animals.txt containing the following animals:

```
Cat
Dog
Dog
Elephant
Fish
Fish
Giraffe
Horse
```

To display only the unique lines that are not duplicated, use the uniq -u command:

```shell
uniq -u animals.txt
```

The output will show the unique animals:

```
Cat
Elephant
Giraffe
Horse
```

Keep in mind that uniq works on sorted files. If your input file is not sorted, first use the sort command and then pipe the output to uniq -u:

```shell
sort unsorted_animals.txt | uniq -u
```

In summary, the uniq command is a helpful tool for filtering out duplicate lines in sorted text files. Combining it with the sort command enables you to process unsorted files and display unique content effectively.
