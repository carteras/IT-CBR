# Exceptions

## Topics covered

"At the end of this learning brief, you will be able to answer the following questions"

* What are exceptions? 
* How do you handle a known exception to a problem in your code?
* How can you handle unexpected errors in your code? 
* How do you create code that only executes if the try is successful? 
* How do you fail silently? 

## Learning Resources

* [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
* [Lecture Video](https://www.youtube.com/watch?v=nlCKrKGHSSk)

## Content

Python uses special objects called exceptions to manage errors that arise during
a program’s execution. Whenever an error occurs that makes Python
unsure what to do next, it creates an exception object. If you write code
that handles the exception, the program will continue running. If you don’t
handle the exception, the program will halt and show a traceback, which
includes a report of the exception that was raised.

Exceptions are handled with try-except blocks. A try-except block asks
Python to do something, but it also tells Python what to do if an exception
is raised. When you use try-except blocks, your programs will continue
running even if things start to go wrong. Instead of tracebacks, which can
be confusing for users to read, users will see friendly error messages that
you write.

### Handling the ZeroDivisionError Exception

```python
print(5/0)
```

```text
Traceback (most recent call last):
File "division.py", line 1, in <module>
print(5/0)
ZeroDivisionError: division by zero
```

The error reported at in the traceback, ZeroDivisionError, is an exception
object. Python creates this kind of object in response to a situation
where it can’t do what we ask it to. When this happens, Python stops the
program and tells us the kind of exception that was raised. We can use this
information to modify our program. We’ll tell Python what to do when this
kind of exception occurs; that way, if it happens again, we’re prepared.


## Topics

### Using try-except Blocks

When you think an error may occur, you can write a try-except block to
handle the exception that might be raised. You tell Python to try running
some code, and you tell it what to do if the code results in a particular kind
of exception

Here’s what a try-except block for handling the ZeroDivisionError exception
looks like:

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```
We put print(5/0), the line that caused the error, inside a try block. If
the code in a try block works, Python skips over the except block. If the code
in the try block causes an error, Python looks for an except block whose
error matches the one that was raised and runs the code in that block.
In this example, the code in the try block produces a ZeroDivisionError,
so Python looks for an except block telling it how to respond. Python then
runs the code in that block, and the user sees a friendly error message
instead of a traceback:

You can't divide by zero!

If more code followed the try-except block, the program would continue
running because we told Python how to handle the error. Let’s look at an
example where catching an error can allow a program to continue running.

### Using Exceptions to Prevent Crashes

Handling errors correctly is especially important when the program has
more work to do after the error occurs. This happens often in programs
that prompt users for input. If the program responds to invalid input appropriately,
it can prompt for more valid input instead of crashing.

Let’s create a simple calculator that does only division:

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
```

This program prompts the user to input a first_number and, if the
user does not enter q to quit, a second_number. We then divide these two
numbers to get an answer w. This program does nothing to handle errors,
so asking it to divide by zero causes it to crash:

```text
Give me two numbers, and I'll divide them.
Enter 'q' to quit.
First number: 5
Second number: 0
Traceback (most recent call last):
File "division.py", line 9, in <module>
answer = int(first_number) / int(second_number)
ZeroDivisionError: division by zero
```

It’s bad that the program crashed, but it’s also not a good idea to let
users see tracebacks. Nontechnical users will be confused by them, and in
a malicious setting, attackers will learn more than you want them to know
from a traceback. For example, they’ll know the name of your program
file, and they’ll see a part of your code that isn’t working properly. A skilled
attacker can sometimes use this information to determine which kind of
attacks to use against your code.

### The else Block

We can make this program more error resistant by wrapping the line that
might produce errors in a try-except block. The error occurs on the line
that performs the division, so that’s where we’ll put the try-except block.
This example also includes an else block. Any code that depends on the try
block executing successfully goes in the else block:

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except:
        print("You can't divide by 0!")
    else:
        print(answer)
```
We ask Python to try to complete the division operation in a try
block, which includes only the code that might cause an error. Any
code that depends on the try block succeeding is added to the else block.
In this case if the division operation is successful, we use the else block to
print the result.

The except block tells Python how to respond when a ZeroDivisionError
arises. If the try statement doesn’t succeed because of a division by
zero error, we print a friendly message telling the user how to avoid this
kind of error. The program continues to run, and the user never sees a
traceback:


```text
Give me two numbers, and I'll divide them.
Enter 'q' to quit.
First number: 5
Second number: 0
You can't divide by 0!
First number: 5
Second number: 2
2.5
First number: q
```
The try-except-else block works like this: Python attempts to run the
code in the try statement. The only code that should go in a try statement
is code that might cause an exception to be raised. Sometimes you’ll have
additional code that should run only if the try block was successful; this
code goes in the else block. The except block tells Python what to do in case
a certain exception arises when it tries to run the code in the try statement.

By anticipating likely sources of errors, you can write robust programs
that continue to run even when they encounter invalid data and missing
resources. Your code will be resistant to innocent user mistakes and malicious
attacks.

### Handling the FileNotFoundError Exception

One common issue when working with files is handling missing files. The
file you’re looking for might be in a different location, the filename may
be misspelled, or the file may not exist at all. You can handle all of these
situations in a straightforward way with a try-except block.

Let’s try to read a file that doesn’t exist. The following program tries
to read in the contents of Alice in Wonderland, but I haven’t saved the file
alice.txt in the same directory as alice.py:

```python
filename = 'alice.txt'
with open(filename) as f_obj:
    contents = f_obj.read()
```

Python can’t read from a missing file, so it raises an exception:

```text
Traceback (most recent call last):
    File "alice.py", line 3, in <module>
        with open(filename) as f_obj:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
```

The last line of the traceback reports a FileNotFoundError: this is the
exception Python creates when it can’t find the file it’s trying to open. In
this example, the open() function produces the error, so to handle it, the try
block will begin just before the line that contains open():

```python
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError: 
    print(f"Sorry, the file {filename} does not exist")
```

In this example, the code in the try block produces a FileNotFoundError,
so Python looks for an except block that matches that error. Python then
runs the code in that block, and the result is a friendly error message
instead of a traceback:

```text
Sorry, the file alice.txt does not exist.
```

The program has nothing more to do if the file doesn’t exist, so the
error-handling code doesn’t add much to this program. Let’s build on this
example and see how exception handling can help when you’re working
with more than one file.

### Analyzing Text

```python
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError: 
    print(f"Sorry, the file {filename} does not exist")
else: 
    print(f"The file {filename} has about {str(len(contents.split(" ")))} words")
```

I moved the file alice.txt to the correct directory, so the try block will
work this time. At u we take the string contents, which now contains the
entire text of Alice in Wonderland as one long string, and use the split()
method to produce a list of all the words in the book. When we use len() on
this list to examine its length, we get a good approximation of the number
of words in the original string v. At w we print a statement that reports
how many words were found in the file. This code is placed in the else block
because it will work only if the code in the try block was executed successfully.
The output tells us how many words are in alice.txt:

### Failing silently

In the previous example, we informed our users that one of the files
was unavailable. But you don’t need to report every exception you catch.
Sometimes you’ll want the program to fail silently when an exception occurs
and continue on as if nothing happened. To make a program fail silently, you
write a try block as usual, but you explicitly tell Python to do nothing in the
except block. Python has a pass statement that tells it to do nothing in a block:

```python
def count_words(filename):
"""Count the approximate number of words in a file."""
try:
    # ...snip...
except FileNotFoundError:
    pass
else:
    # ...snip...

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
```

The only difference between this listing and the previous one is the
pass statement at u. Now when a FileNotFoundError is raised, the code in
the except block runs, but nothing happens. No traceback is produced,
and there’s no output in response to the error that was raised. Users see
the word counts for each file that exists, but they don’t see any indication
that a file was not found:

## Practice Questions

### Practice Question 1: Addition:

One common problem when prompting for numerical input occurs when people provide text instead of numbers. When you try to convert the input to an int, you’ll get a TypeError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.

### Practice Question 2: Addition Calculator:

Wrap your code from above in a while loop so the user can continue entering numbers even if they have made a mistake. Make sure you test it by entering text instead of a number

### Practice Question 3: Cats and Dogs:

Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block
executes properly.


### Practice Question 4: Silent Cats and Dogs:

Modify your except block from the previous code to fail silently if either file is missing. 

### Practice Question 5: Common Words



## Mastery Question

### Mastery Question 1

Visit Project Gutenberg (http://gutenberg.org/ )
and find 5 texts you’d like to analyse. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.
You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:

```python
line = "Row, row, row your boat"
line.count('row')
line.lower().count('row')
```

Notice that converting the string to lowercase using lower() catches
all appearances of the word you’re looking for, regardless of how it’s
formatted.

Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text.
