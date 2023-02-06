# How do we make decisions in python?

In Python, conditions are used to make decisions in the code by evaluating whether a statement is True or False.

## Learning Goals

*By the end of this module you should be able to answer the following:*

* You will know what comparison operators are: 
  * ==
  * !=
  * <
  * \>
  * <=
  * \>=
  * not
  * is
  * and
  * or
  * in
* What a Boolean value is
* The if statement
* The if-else statement
* the if-elif-else statement

## Code

*It is important to practice code and challenge our brain in new ways. Do all of the problems below, including the example problems. They will make you a better programmer.*

### Comparison Operators

These include "==" (equal to), "!=" (not equal to), "<" (less than), ">" (greater than), "<=" (less than or equal to), and ">=" (greater than or equal to).

### Boolean Values

There are only two Boolean values in Python, True and False, which are used to represent the truth value of an expression.

### The if Statement

The if statement is used to execute a block of code only if a certain condition is met. The syntax is:

```python

if condition:
    # Code to execute if condition is True

```

### The if-else Statement

The if-else statement is used to execute one block of code if a condition is True, and another block of code if it is False. The syntax is:

```python
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
```

### The if-elif-else Statement

The if-elif-else statement is used to execute different blocks of code based on multiple conditions. The syntax is:

```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition1 is False and condition2 is True
else:
    # Code to execute if both condition1 and condition2 are False
```

### Boolean logic

Boolean logic in Python refers to the use of the bool data type and the operations and, or, and not to represent and manipulate truth values (True or False). These truth values are used in conditions to make decisions in the code.

The bool data type: In Python, a bool value can either be True or False. The bool type is used to represent truth values and is often used in conditions to make decisions in the code.

The and operator: The and operator is used to evaluate two conditions and return True if both conditions are True, otherwise it returns False. The syntax is:

```bash
condition1 and condition2
```

The or operator: The or operator is used to evaluate two conditions and return True if at least one of the conditions is True, otherwise it returns False. The syntax is:

```bash
condition1 or condition2
```

The not operator: The not operator is used to invert a truth value. If the condition is True, not returns False, and if the condition is False, not returns True. The syntax is:

```bash
not condition
```

```python
x = 5
y = 10

print(x > 2 and y < 20) # True
print(x < 2 or y > 20) # False
print(not x > 2) # False
```

### The in keyword 

```python
test_string = "ada"
if ('d' in test_string):
    print(f"d is in {test_string}")
```

## Examples

### Checking for equality

```python
x = 5
if x == 5:
    print("x is 5")
```

Output: x is 5

### Checking for multiple conditions

```python
x = 10
if x > 5 and x < 15:
    print("x is between 5 and 15")
```

Output: x is between 5 and 15


### Using the else clause 

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

Output: x is not greater than 5

### using the elif clause

```python
x = 7
if x < 5:
    print("x is less than 5")
elif x > 5 and x < 10:
    print("x is between 5 and 10")
else:
    print("x is greater than or equal to 10")
```

Output: x is between 5 and 10

## Practice Questions


### Practice

* Check if a number provided by a user is positive
* Check to see if a string provided by a user is empty
* Check to see if a given number provided by a user is odd or even
* Check to see if a given number provided by a user is between 0 and 10 or between 20 and 30
* check to see if a given string provided by a user has both the letters a and b
* check to see if a given number provided by a user is positive and its square is greater than 100
* Check if a year is divisible by 4, but not divisible by 100 unless it is divisible by 400

## Fluff about find out

So, you've learnt lots of things so far today. I challenge you to use your imagination and try and find some things that you feel you might be able to do, but weren't necessarily taught.

Because it's our first week, I am happy to give you some hints to start you off, but go nuts. 

* Can we check to see if a letter provided by a user is a known vowel without making a giant if-elif-else statement?
* Can we check to see if a year provided by a user is a leap year? 


## Bug hunt

Kevin has written some code and it doesn't work. What's wrong with it?

```python
num == int(input("Enter a positive or negative number: "))
if num <= 0:
    if num == 0
        print('The number is zero.")
   elif:
        print("The number is positive.")
else:
    print("The number is negative.")
```
