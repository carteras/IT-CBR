# Iteration

## Learning Goals

*By the end of this module you should be able to answer the following:*

* What is Iteration?
* What is a while loop?

# Code

*It is important to practice code and challenge our brain in new ways. Do all of the problems below, including the example problems. They will make you a better programmer.*

## Example Problems

*Example problems are best if you code them up yourself and store them. Don't just copy and paste, code them in and make them work. If you are really smart about it, you'll remake them slightly differently to really establish your learning.*

### Problem: We want to keep doing something until some condition is met

There are times where you might need to keep doing something while some condition is true. Take the following diagram as a reference: 

![](2022-02-04-10-19-15.png)

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

### Problem: I want to do something n number of times but no more. 

```python
i = 0
while i < 10:
    print(i)
    i = i + 1
```

```python
for i in range(0, 10):
    print(i)
```

## Practice Problems

*Practice questions are essential to mastering a skill. Often, you will be asked to do things you haven't exactly done yet, or not at all. Be challenged by it and see if you can get google, the person next to you, or the teacher, to help before you stop working.*


### The times table

Create the following output. You must use a while loop. You must be able to do the times tables of any integer between any starting point and end point.

Potential viable tests:

* 5 times tables from 1 - 5
* 23 times tables from 100 to 100,000
* 1 times tables from -50 to +50

```text
Time tables goodness
which times table do you want? 5
Where do you want to start? 1
Where do you want to end? 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
```

### Abusing while loops

Using while loops, expand the starter code to create the following shapes.

```python
shape = "*"
```

output1:

```bash
*
**
***
****
```

output2:

```text
*
***
******
***
*
```

### Factorials

A factorial the product of an integer and all the integers below it; e.g. factorial four ( 4! ) is equal to 4\*3\*2\*1 = 24.

Find the factorial for any number: 

```python
factorial = input("Find the factorial for the number: ")
# your code here
```

### Average 

The average is the sum of numbers divided by the number of numbers. Create a program that will continually take numbers from the user until the user presses `q`. Then it prints the average of all of the numbers given. 

```python
playing = True
# some of your code will go here
while playing:
    user_input = ("Add a number to add the the sum. Press q to finish. " )
    # some more of your code goes here
```

