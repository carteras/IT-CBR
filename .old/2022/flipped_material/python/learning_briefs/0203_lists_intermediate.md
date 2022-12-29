# Intermediate Lists

## Learning Goals

*By the end of this module you should be able to answer the following:*

* How to work with only a part of a list
* Creating numerical lists

## Revision

### Fix this broken code

#### Revision 1: writing what now?

Chad wants to write a file of usernames and passwords. He wants the written format of the file to be the following:

```
passwords.txt
name:password
name:password
```

Chad's code is below:

```python
names = ['ada", 'bob', 'charlie', `erin`]
passwords = [123456, 123455678, password, qwerty ,123456789]
with open("foo") as file_handler:
  for i in enumerate(names):
    file_handler.write(b"{names[i]};{passwords{i}")
```

#### Revision 2: What are functions?

Someone told Chad that passwords should be "hashed". Chad has found the hash library for python and chosen the MD5 protocol because it looks easy to use.

```python
from hashlib import md5

str hash_password(password)
  return md5(pass.encode()),hexdigest()

passwords = {123456, 123455678, "password", "qwerty" ,123456789}

for password in passwords;
    print(hash_password(password))

```

## Code

*It is important to practice code and challenge our brain in new ways. Do all of the problems below, including the example problems. They will make you a better programmer.*

### Example Problems

*Example problems are best if you code them up yourself and store them. Don't just copy and paste, code them in and make them work. If you are really smart about it, you'll remake them slightly differently to really establish your learning.*

#### Problem: You want to create a series of numbers and loop through them

Many reasons exist to store a set of numbers. For example, you’ll need to
keep track of the positions of each character in a game, and you might want
to keep track of a player’s high scores as well. In data visualizations, you’ll
almost always work with sets of numbers, such as temperatures, distances,
population sizes, or latitude and longitude values, among other types of
numerical sets.

Lists are ideal for storing sets of numbers, and Python provides a number
of tools to help you work efficiently with lists of numbers. Once you
understand how to use these tools effectively, your code will work well even
when your lists contain millions of items.

```python
for value in range(1, 5):
    print(value)
```

Although this code looks like it should print the numbers from 1 to 5, it
doesn’t print the number 5:

```text
1
2
3
4
```

In this example, range() prints only the numbers 1 through 4. This is
another result of the off-by-one behaviour you’ll see often in programming
languages. The range() function causes Python to start counting at the first
value you give it, and it stops when it reaches the second value you provide.
Because it stops at that second value, the output never contains the end
value, which would have been 5 in this case.

To print the numbers from 1 to 5, you would use range(1,6):

```python
for value in range(1, 6):
    print(value)
```

This time the output starts at 1 and ends at 5:

```text
1
2
3
4
5
```

If your output is different than what you expect when you’re using
range(), try adjusting your end value by 1.

#### Problem: You need to make a list of numbers

If you want to make a list of numbers, you can convert the results of range()
directly into a list using the list() function. When you wrap list() around a
call to the range() function, the output will be a list of numbers.
In the example in the previous section, we simply printed out a series of
numbers. We can use list() to convert that same set of numbers into a list:

```python
numbers = list(range(1, 6))
print(numbers)
```

> [1, 2, 3, 4, 5]

#### Problem: You want a list of even numbers

We can also use the range() function to tell Python to skip numbers
in a given range. For example, here’s how we would list the even numbers
between 1 and 10:

```python
even_numbers = list(range(2,11,2))
print(even_numbers)
```

In this example, the range() function starts with the value 2 and then
adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end
value, 11, and produces this result:

> [2, 4, 6, 8, 10]

You can create almost any set of numbers you want to using the range()
function. For example, consider how you might make a list of the first 10
square numbers (that is, the square of each integer from 1 through 10). In
Python, two asterisks (**) represent exponents. Here’s how you might put
the first 10 square numbers into a list:

```python
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
```

> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#### Problem: You only want to work with part of a list 

You learned how to access single elements in a list, and in this
chapter you’ve been learning how to work through all the elements in a list.
You can also work with a specific group of items in a list, which Python calls
a slice.

Slicing a List
To make a slice, you specify the index of the first and last elements you
want to work with. As with the range() function, Python stops one item
before the second index you specify. To output the first three elements
in a list, you would request indices 0 through 3, which would return elements
0, 1, and 2.
The following example involves a list of players on a team:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```

> ['charles', 'martina', 'michael']

You can generate any subset of a list. For example, if you want the second,
third, and fourth items in a list, you would start the slice at index 1 and
end at index 4:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
```

> ['martina', 'michael', 'florence']

If you omit the first index in a slice, Python automatically starts your
slice at the beginning of the list:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
```

> ['charles', 'martina', 'michael', 'florence']

#### Problem: You want to loop through a sliced list

You can use a slice in a for loop if you want to loop through a subset of
the elements in a list. In the next example we loop through the first two
players and print their names as part of a simple roster:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
    for player in players[1:3]:
print(player.title())
```

> Here are the first two players on my field
> Martina
> Michael

### Practice Problems

*Practice questions are essential to mastering a skill. Often, you will be asked to do things you haven't exactly done yet, or not at all. Be challenged by it and see if you can get google, the person next to you, or the teacher, to help before you stop working.*


#### Practice 1: Counting to Twenty

Use a for loop to print the numbers from 1 to 20

#### Practice 2: One million

Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing ctrl - C)

#### Practice 3 Summing a Million

Make a list of the numbers from one to one million,and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

#### Practice 4:  Odd Numbers

Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

#### Practice 5: Three

Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.

#### Practice 6 Cubes

A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
