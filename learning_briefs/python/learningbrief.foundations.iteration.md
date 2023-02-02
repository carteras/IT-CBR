# Iteration 

"Iterate Your Way to Efficient Programming with Python Loops."

## Learning Goals

*By the end of this module you should be able to answer the following:*

1. The purpose of iteration: Repeat a process multiple times until a certain condition is met.
2. The two main types of loops in Python: `for` and `while`.
3. The syntax of a `for` loop
4. The syntax of a `while` loop
5. The importance of a `counter` or loop variable
6. The importance of using a `break` statement
7. The importance of using a `continue` statement

## What is iteration?

Iteration is a way of repeating a process multiple times in programming. It's like doing a task repeatedly, until a certain condition is met. For example, if you want to print the numbers 1 to 10, you can use a loop to repeat the process of printing a number 10 times, instead of writing the print statement 10 times. In Python, you can use a `for` loop to repeat a block of code for a specific number of times or you can use a `while` loop to repeat the code until a certain condition is met. This is a fundamental concept in programming and is used widely in various algorithms and applications.

## Code

*It is important to practice code and challenge our brain in new ways. Do all of the problems below, including the example problems. They will make you a better programmer.*

### for loop

The for loop is used to repeat a block of code for a specific number of times. The loop variable is defined and assigned values from a sequence (e.g. list or range).

```python
# Example: Print numbers 1 to 10 using a for loop
for i in range(1, 11):
    print(i)
```

In this example, the for loop is used to repeat the process of printing a number 10 times. The range function generates a sequence of numbers from 1 to 10 (exclusive of 11), and the loop variable `i` takes on the values of this sequence one by one in each iteration. The code inside the loop is executed for each value of `i` and the result is:

```bash
2
3
4
5
6
7
8
9
10
```

### while loops 

```python
# Example: Print numbers 1 to 10 using a while loop
counter = 1
while counter <= 10:
    print(counter)
    counter += 1
```
n this example, the while loop is used to repeat the process of printing a number 10 times. The loop condition counter <= 10 is checked before each iteration, and if the condition is true, the code inside the loop is executed. The variable counter is used to keep track of the number of iterations and control the loop. The code inside the loop increments the value of counter by 1 in each iteration. The result is:

```bash
1
2
3
4
5
6
7
8
9
10
```

### The break statement

The break statement in Python is used to exit a loop prematurely. When a break statement is executed inside a loop, it terminates the loop immediately, skipping any remaining iterations. The program then continues with the first statement after the loop.

```python
# Example: Find the first multiple of 7 using a for loop and break statement
for i in range(1, 100):
    if i % 7 == 0:
        print(f"The first multiple of 7 is {i}")
        break
```

The for loop is used to repeat the process of checking if `i` is a multiple of 7 for the numbers in the range from 1 to 100. The loop variable `i` takes on the values of this range one by one in each iteration. If `i` is a multiple of 7, the code inside the loop prints the value of `i` and the break statement is used to break out of the loop prematurely. 

```python
# Example: Find the first multiple of 7 using a while loop and break statement
counter = 1
while True:
    if counter % 7 == 0:
        print(f"The first multiple of 7 is {counter}")
        break
    counter += 1
```

The while loop is used to repeat the process of checking if counter is a multiple of 7 until the condition is met. The loop condition True always evaluates to True, so the loop will keep repeating until the break statement is encountered. If counter is a multiple of 7, the code inside the loop prints the value of counter and the break statement is used to break out of the loop prematurely.

### the continue statement

The continue statement in Python is used to skip the current iteration of a loop and move on to the next one. When a continue statement is encountered inside a loop, it skips any remaining statements in the current iteration and immediately begins the next iteration.

Here's an example of using a `continue` statement in a `for` loop without using lists or other data structures:

```python
# Example: Print only odd numbers using a for loop and continue statement
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)
```

In this example, the for loop is used to iterate over the numbers in the range from 1 to 10. If the value of `i` is an even number (that is, `if i % 2 == 0`), the continue statement is executed, and the current iteration is skipped.

Here's an example of using a `continue` statement in a `while` loop:

```python
# Example: Print only odd numbers using a while loop and continue statement
counter = 1
while counter < 10:
    if counter % 2 == 0:
        counter += 1
        continue
    print(counter)
    counter += 1
```

In this example, the `while` loop is used to repeat the process of checking if `counter` is an odd number and printing it until `counter` is no longer less than 10. If `counter` is an even number, the continue statement is executed, and the current iteration is skipped. The next iteration starts immediately.



## Examples

*Example problems work best if you code them up yourself and store them. Don't just copy and paste, code them in and make them work. If you are really smart about it, you'll remake them slightly differently to really establish your learning.*

### Example: We want to keep doing something until some condition is met

There are times where you might need to keep doing something while some condition is true. Take the following diagram as a reference: 

![](img/2022-02-04-10-19-15.png)

1. answer is assigned to the string `"no"`
2. if answer is equivalent to `"no"` then go to 3 else go to 6
3. write `"are we there yet"` to console
4. wait for user input
5. Go to 2
6. print "huzzah

We can solve this with the while loop. 

```python
answer == 'no'
while answer == 'no'
    answer = input("Are we there yet? ")
print("huzzah")
```

### Example: I want to do something n number of times but no more

Let's say that for some reason, you need your computer to count from 0 to 9. How can we do it? 

```python
i = 0                  # set i to be 0
while i < 10:          # keep looping while i is less than 10
    print(i)           # print i
    i = i + 1          # assign i to whatever i is + 1
```

```python
for i in range(0, 10): # we can use the range function define our starting and end
    print(i)           # print the current value of i
```

The `range` function in Python generates a sequence of numbers, starting from 0 by default, and increments by 1 (also by default), and stops before a specified number. The `range` function is often used in for loops to repeat a set of statements a specified number of times.

## Practice Questions

*Practice questions are essential to mastering a skill. Often, you will be asked to do things you haven't exactly done yet, or not at all. Be challenged by it and see if you can get google, the person next to you, or the teacher, to help before you stop working.*

* Write a for loop that prints the numbers from 10 to 1 in reverse order.
* Write a for loop that counts the number of even numbers in the range from 1 to 10 and prints the result.
* Write a for loop that calculates the sum of the squares of all the numbers from 1 to 10 and prints the result.
* Write a for loop that prints the numbers from 20 to 30.
* Write a for loop that calculates the sum of all the numbers from 1 to 100 and prints the result.
* Write a for loop that prints the numbers from 1 to 10, but stops when it reaches a number greater than 5
* Write a for loop that calculates the sum of all the even numbers in the range from 1 to 10, but skips over the number 6.
* Write a for loop that counts the number of odd numbers in the range from 1 to 20, but stops when it reaches 5 odd numbers.
* Write a while loop that prints the numbers from 1 to 10.
* Write a while loop that calculates the sum of all the even numbers in the range from 1 to 10, but skips over the number 6.
* Write a while loop that counts the number of odd numbers input by the user, but stops when the user inputs 0.
* Write a while loop that prints the squares of all the numbers from 1 to 5, but stops when it reaches a number greater than 25.
* Write a while loop that calculates the factorial of a number input by the user, but stops when the user inputs a negative number.

## Fluff about find out

So, you've learnt lots of things so far today. I challenge you to use your imagination and try and find some things that you feel you might be able to do, but weren't necessarily taught.

Because it's our first week, I am happy to give you some hints to start you off, but go nuts. 

* Can we use lists inside lists?
* Can we loop through strings backwards?
* Can we write a program that makes the 1-n times tables for a given number?
  * Time tables goodness
  * which times table do you want? 5
  * Where do you want to start? 1
  * Where do you want to end? 5
  * 5 * 1 = 5
  * 5 * 2 = 10
  * 5 * 3 = 15
  * 5 * 4 = 20
  * 5 * 5 = 25
* Can you use loops to get numerical input from a user and find the sum of all of the numbers entered (use q to finish)
* Actually, could you also calculate the average?


## Bug hunt

Kevin has written some code and it doesn't work. What's wrong with it?

Kevin wants to write a program that makes the following shape: 

```bash
*
**
***
****
***
**
*
```

This is his code: 

```python
for i in range(1, 4):
    print("*" * 1)

for i in range(4, 1):
    print("*" * i)
```

What is wrong with it?
