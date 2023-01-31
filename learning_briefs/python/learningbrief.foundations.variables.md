# Strings, Variables, and Operations in Python 

## Learning Goals

*By the end of this module you should be able to answer the following:*

* In python, how do you print a string to the console?
* If you had to, how would you store something to memory?
* How do you join two strings together?
* How would you format a string so variables join neatly?
* How would you capture user input?
* Can you convert user input into other data types?
* How do you add/subtract/multiply/divide numbers together?

## Examples

### Problem: We want to print a simple string

We can use the print function to print most data types to the standard console.

```python
print("hello world")
```

### Problem: we need to store something in a variable and then print it

You can store your data in a variable.

```python
foo = "output"
print(foo)
```

A variable acts as a label so you can tell the computer what block of memory to get.

### Problem: We want to join two strings together

We can concatenate strings together or be super lazy and just be a comma between to printable data types. NOTE: commas work in python. Your mileage may vary in other languages.

```python
print("Ada" + "Lovelace")
print("Ada", "Lovelace")
```

### Problem: I want to put a variable in a complex string. Can I format variables into strings?  

You can use f-strings. To declare a string is an f-string  you put an f on the outside of the string.

```python
given_name = "Ada"
family_name = "Lovelace"
print(f"The first programmer's name was {given_name} {family_name}")
```

NOTE: f-strings don't just live in print statements:

```python
given_name = "Ada"
family_name = "Lovelace"
out = f"The first programmer's name was {given_name} {family_name}"
print(out)
```

### Problem: How can I do some maths calculations?

The true maths games!

```python
print(3+2) # 3 + 2 = 5
print(3-2) # 3 - 2 = 1
print(3*2) # 3 * 2 = 6
print(3/2) # 3 / 2 = 1.5 (be careful of old versions)
print(3**2)# 3^2 = 3*3 = 9
print(3%2) # 3%2 = 1 (3/2 = 1 with 1 remaining
```

NERD ALERT! What's going on with that % operator? It's weird, right?

### Problem: I want to get a users input?

You can use the input function.

```python
name = input('Hey, what is your name?")
print(name)
```

### Problem: I want to capture data, like a number, but input only captures strings. 

We can convert types by using a built it function. If we want to turn a string to an integer we would use `int("5")`

```python
foo = input("How many days are in the week? ")
foo = int(foo)
print(foo*3)
```

## Practice Questions

You can do all of these in the same piece of code

### Create a code block that prints out the following text:

1. "Hello world"
2. "Hello again"
3. "Printing is fun!"
4. "Yay! Printing"

### Given the following variables produce the required output

```python
hens = 25 + 30/6  
roosters = 100 - 25 * 3  
```

print the following output  

```bash
"I will now count my chickens"
"I have 30.0 hens and 25 Rosters" 
```

### Create a program with the following variables

```python
cars = 100
space_in_cars = 4  # excluding the driver
drivers = 30 
passengers = 90
```

The program must calculate:

1. How many cars, if any, aren't needed?
2. What is the maximum number of passengers can you physically drive?
3. The average number of passengers per car

### Calendar wonder land

You are to create a program that can accept user input and display it. The program that you ask to write asks a user for the following input:

* Their given name
* The day of their birth
* The month of their birth
* The year of their birth

Your program must calculate an approximation* of how many days that person has been alive and then output it in the following format:

`"Hi {given_name}, you have been alive for approximately {n_days}"`

NOTE: calculating the exact number of days isn't trivial. An approximation is fine. Don't over think it. 

## Fluff about find out

So, you've learnt lots of things so far today. I challenge you to use your imagination and try and find some things that you feel you might be able to do, but weren't necessarily taught.

Because it's our first week, I am happy to give you some hints to start you off, but go nuts. 

* Can you make python change a string (the stuff between "" or '') to upper case?
* What happens if you multiply a string?
* What happens if you divide a string?
* What's the difference between `print("foo", "bar")` `print("foo" + "bar")` and `print(f"{foo} {bar}")`?


## Bug hunt

Kevin has written some code and it doesn't work. What's wrong with it? 

```python

foo = input("Type a number: ')
if foob == input('Type a number'):
    pornt("You are a winner")
else: print("hey hey, try again")
```
