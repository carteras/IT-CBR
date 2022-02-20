# Dictionaries

## Learning Goals

*By the end of this module you should be able to answer the following:*



## Concepts

Understanding dictionaries allows you to model a variety of real-world
objects more accurately. You’ll be able to create a dictionary representing a
person and then store as much information as you want about that person.
You can store their name, age, location, profession, and any other aspect of
a person you can describe. You’ll be able to store any two kinds of information
that can be matched up, such as a list of words and their meanings, a
list of people’s names and their favourite numbers, a list of mountains and
their elevations, and so forth.

Consider a game featuring aliens that can have different colours and point
values. This simple dictionary stores information about a particular alien:

```python
alien_0 = {'colour': 'green', 'points': 5}
print(alien_0['colour'])
print(alien_0['points'])
```

> green
> 5

As with most new programming concepts, using dictionaries takes
practice. Once you’ve worked with dictionaries for a bit you’ll soon see how
effectively they can model real-world situations.


### Working with Dictionaries

A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key.
A key’s value can be a number, a string, a list, or even another dictionary.
In fact, you can use any object that you can create in Python as a value in a
dictionary.

In Python, a dictionary is wrapped in braces, {}, with a series of key-value
pairs inside the braces, as shown in the earlier example:

```python
alien_0 = {'colour': 'green', 'points': 5}
```

A key-value pair is a set of values associated with each other. When you
provide a key, Python returns the value associated with that key. Every key
is connected to its value by a colon, and individual key-value pairs are separated
by commas. You can store as many key-value pairs as you want in a
dictionary.

The simplest dictionary has exactly one key-value pair, as shown in this
modified version of the alien_0 dictionary

```python
alien_0 = {'colour': 'green'}
```

This dictionary stores one piece of information about alien_0, namely
the alien’s colour. The string 'colour' is a key in this dictionary, and its associated
value is 'green'.

### Accessing Values in a Dictionary

To get the value associated with a key, give the name of the dictionary and
then place the key inside a set of square brackets, as shown here:

```python
alien_0 = {'colour': 'green'}
print(alien_0['colour'])
```

> green

You can have an unlimited number of key-value pairs in a dictionary.
For example, here’s the original alien_0 dictionary with two key-value pairs:

```python
alien_0 = {'colour': 'green', 'points': 5}
```

Now you can access either the colour or the point value of alien_0. If a
player shoots down this alien, you can look up how many points they should
earn using code like this:

```python
alien_0 = {'colour': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {str(new_points)} points!)
```

> You just earned 5 points!

### Adding New Key-Value Pairs

Dictionaries are dynamic structures, and you can add new key-value pairs
to a dictionary at any time. For example, to add a new key-value pair, you
would give the name of the dictionary followed by the new key in square
brackets along with the new value.

Let’s add two new pieces of information to the alien_0 dictionary: the
alien’s x- and y-coordinates, which will help us display the alien in a particular
position on the screen. Let’s place the alien on the left edge of the
screen, 25 pixels down from the top. Because screen coordinates usually
start at the upper-left corner of the screen, we’ll place the alien on the left edge of the screen by setting the x-coordinate to 0 and 25 pixels from the
top by setting its y-coordinate to positive 25, as shown here:

```python
alien_0 = {'colour': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

> {'colour': 'green', 'points': 5}
> {'colour': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}

The final version of the dictionary contains four key-value pairs. The
original two specify color and point value, and two more specify the alien’s
position. Notice that the order of the key-value pairs does not match the
order in which we added them. Python doesn’t care about the order in
which you store each key-value pair; it cares only about the connection
between each key and its value.

#### Starting with an empty dictionary

It’s sometimes convenient, or even necessary, to start with an empty dictionary
and then add each new item to it. To start filling an empty dictionary,
define a dictionary with an empty set of braces and then add each key-value
pair on its own line. For example, here’s how to build the alien_0 dictionary
using this approach:

```python
alien_0 = {}
alien_0['colour'] = 'green'
alien_0['points'] = 5
print(alien_0)
```

> {'color': 'green', 'points': 5}



### Modifying Values in a Dictionary

To modify a value in a dictionary, give the name of the dictionary with the
key in square brackets and then the new value you want associated with
that key. For example, consider an alien that changes from green to yellow
as a game progresses:

```python
alien_0 = {'colour': 'green'}
print("The alien is " + alien_0['colour'] + ".")
alien_0['colour'] = 'yellow'
print("The alien is now " + alien_0['colour'] + ".")
```

> The alien is green.
> The alien is now yellow.

### Looping Through a Dictionary

You already know how to access any given value from a known key. Consider the following dictionary. What is Elizabeth Feinler's password?

```python
users = {
    'ada_lovelace': "e10adc3949ba59abbe56e057f20f883e",
    'bob_kahn': "25f9e794323b453885f5181f1b624d0b",
    'charles_babbage': "827ccb0eea8a706c4c34a16891f84e7b",
    'elizabeth_feinler': 'd8578edf8458ce06fbc5bb76a58c5ca4',
    'frances_allen':, '5f4dcc3b5aa765d61d8327deb882cf99'
}
print(f'password: {users['elizabeth_feinler]}')
```

> password: d8578edf8458ce06fbc5bb76a58c5ca4


What if we don't know what the keys are in our list? How can we access the keys/values dynamically? 

```python
users = {
    'ada_lovelace': "e10adc3949ba59abbe56e057f20f883e",
    'bob_kahn': "25f9e794323b453885f5181f1b624d0b",
    'charles_babbage': "827ccb0eea8a706c4c34a16891f84e7b",
    'elizabeth_feinler': 'd8578edf8458ce06fbc5bb76a58c5ca4',
    'frances_allen':, '5f4dcc3b5aa765d61d8327deb882cf99'
}

for key, value in users.items():
    print(f"{key}'s password is {value})
```

## Code

*It is important to practice code and challenge our brain in new ways. Do all of the problems below, including the example problems. They will make you a better programmer.*

### Example Problems

*Example problems are best if you code them up yourself and store them. Don't just copy and paste, code them in and make them work. If you are really smart about it, you'll remake them slightly differently to really establish your learning.*

#### Problem 1: Accessing Values in a Dictionary

```python
users = {
    'ada_lovelace': "e10adc3949ba59abbe56e057f20f883e",
    'bob_kahn': "25f9e794323b453885f5181f1b624d0b",
    'charles_babbage': "827ccb0eea8a706c4c34a16891f84e7b",
    'elizabeth_feinler': 'd8578edf8458ce06fbc5bb76a58c5ca4',
    'frances_allen': '5f4dcc3b5aa765d61d8327deb882cf99'
}
print(users['ada_lovelace'])
```

> e10adc3949ba59abbe56e057f20f883e

#### Problem 2: Adding new key-value pairs

```python
users = {
    'ada_lovelace': "e10adc3949ba59abbe56e057f20f883e",
    'bob_kahn': "25f9e794323b453885f5181f1b624d0b",
    'charles_babbage': "827ccb0eea8a706c4c34a16891f84e7b",
    'elizabeth_feinler': 'd8578edf8458ce06fbc5bb76a58c5ca4',
    'frances_allen': '5f4dcc3b5aa765d61d8327deb882cf99'
}
users['grace_hopper'] = '25d55ad283aa400af464c76d713c07ad'
print(users)
```

> {
>   'ada_lovelace': 'e10adc3949ba59abbe56e057f20f883e',
>   'bob_kahn': '25f9e794323b453885f5181f1b624d0b',
>   'charles_babbage': '827ccb0eea8a706c4c34a16891f84e7b',
>   'elizabeth_feinler': 'd8578edf8458ce06fbc5bb76a58c5ca4',
>   'frances_allen': '5f4dcc3b5aa765d61d8327deb882cf99',
>   'grace_hopper': '25d55ad283aa400af464c76d713c07ad'
> }

#### Problem 3: Modifying Values in a Dictionary

```python
users = {
    'ada_lovelace': "e10adc3949ba59abbe56e057f20f883e",
    'bob_kahn': "25f9e794323b453885f5181f1b624d0b",
    'charles_babbage': "827ccb0eea8a706c4c34a16891f84e7b",
    'elizabeth_feinler': 'd8578edf8458ce06fbc5bb76a58c5ca4',
    'frances_allen': '5f4dcc3b5aa765d61d8327deb882cf99'
}
users['grace_hopper'] = '25d55ad283aa400af464c76d713c07ad'
print(users['grace_hopper'])
users['grace_hopper'] = 'bf08622301b1dc675c6c7e5ada74dbe3'
print(users['grace_hopper'])
```

> 25d55ad283aa400af464c76d713c07ad
> bf08622301b1dc675c6c7e5ada74dbe3

#### Problem 4: Looping Through All Key-Value Pairs

```python
users = {
    'ada_lovelace': "e10adc3949ba59abbe56e057f20f883e",
    'bob_kahn': "25f9e794323b453885f5181f1b624d0b",
    'charles_babbage': "827ccb0eea8a706c4c34a16891f84e7b",
    'elizabeth_feinler': 'd8578edf8458ce06fbc5bb76a58c5ca4',
    'frances_allen': '5f4dcc3b5aa765d61d8327deb882cf99'
}

for key, value in users.items():
  print(f"{key}: {value}")
```

#### Problem 5: Looping Through All the Keys in a Dictionary

```python
users = {
    'ada_lovelace': "e10adc3949ba59abbe56e057f20f883e",
    'bob_kahn': "25f9e794323b453885f5181f1b624d0b",
    'charles_babbage': "827ccb0eea8a706c4c34a16891f84e7b",
    'elizabeth_feinler': 'd8578edf8458ce06fbc5bb76a58c5ca4',
    'frances_allen': '5f4dcc3b5aa765d61d8327deb882cf99'
}

for key in users:
  print(f"{key}: {users[key]}")
```


#### Problem 6: Looping Through All Values in a Dictionary

```python
users = {
    'ada_lovelace': "e10adc3949ba59abbe56e057f20f883e",
    'bob_kahn': "25f9e794323b453885f5181f1b624d0b",
    'charles_babbage': "827ccb0eea8a706c4c34a16891f84e7b",
    'elizabeth_feinler': 'd8578edf8458ce06fbc5bb76a58c5ca4',
    'frances_allen': '5f4dcc3b5aa765d61d8327deb882cf99'
}

for values in users.values():
  print(f"{values}")
```

> e10adc3949ba59abbe56e057f20f883e
> 25f9e794323b453885f5181f1b624d0b
> 827ccb0eea8a706c4c34a16891f84e7b
> d8578edf8458ce06fbc5bb76a58c5ca4
> 5f4dcc3b5aa765d61d8327deb882cf99
> 
### Practice Problems

*Practice questions are essential to mastering a skill. Often, you will be asked to do things you haven't exactly done yet, or not at all. Be challenged by it and see if you can get google, the person next to you, or the teacher, to help before you stop working.*


#### Practice 1: Person

Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

#### Practice 2: Favourite Numbers

Use a dictionary to store people’s favourite numbers. Think of five names, and use them as keys in your dictionary. Think of a favourite
number for each person, and store each as a value in your dictionary. Print each person’s name and their favourite number. For even more fun, poll a few friends and get some actual data for your program.

#### Practice 3: Glossary

A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

* Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
* Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

#### Practice 4: Glossary 2

Now that you know how to loop through a dictionary, clean up the code from before by replacing your series of print statements with a loop that runs through the dictionary’s keys and values.

When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

#### Practice 5 Rivers

Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

* Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
* Use a loop to print the name of each river included in the dictionary.
* Use a loop to print the name of each country included in the dictionary.

