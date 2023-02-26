# How does something work?

## Learning Goals

> Lists in Python code,
> Store data, keep it in line,
> Efficient and neat.

*By the end of this recipe you should be able to answer the following:*

* Know what Lists are and what common syntax exists to manipulate them
* Gain a broad understanding of how to use lists to solve foundation problems.
* Know what conditions are. 
* Understand how to use simple conditions to make decisions


## Other links that might be useful

* Google for Education: [Lists methods](https://developers.google.com/edu/python/lists)  
* Python-Textbook: [selection control statements](https://python-textbok.readthedocs.io/en/1.0/Selection_Control_Statements.html)

## Concepts

In Python, a list is a built-in data structure that is used to store a collection of items. It is an ordered and mutable sequence of elements, meaning that the elements are stored in a specific order and can be added, removed, or modified. Lists can store different types of data, including integers, strings, and other objects, and they are created using square brackets [] enclosing a comma-separated list of elements. For example, the following code creates a list of integers:

```python
swords = ['mortuary', 'arming', 'long', 'sabre']
print(swords)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
['mortuary', 'arming', 'long', 'sabre']
```

Here, I create a list of strings with the name of various types of swords. I then assign that list of strings to a variable called swords. 

Lists are a versatile and widely used data structure in Python, and they are used in many different applications, including data processing, machine learning, and web development.

## Example

That's great, but how do we use them? 

### Accessing elements in a list 

Lists are ordered collections. This means that they remain in the order that you left them in. By doing this, it becomes possible to access elements in the list if you know it's position or index. 

To access an element in a list, we use the lists variable name followed by the index position of the item in square brackets. 

For example, using my list of sword names, I can access the first sword name. 

```python
swords = ['mortuary', 'arming', 'long', 'sabre']
print(swords[0])
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
mortuary
```

It's important to note here, that indexes start at 0, not 1. This is because the number line starts at 0, not 1.

This use of an element in a list can be used like any other variable. Below, I have an f-string that is using the index position of the first sword.

```python
first_sword = f'My first sword was a {swords[0].title()}.'
print(swords[0])
print(swords[0].title())
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
mortuary
Mortuary
```

### Modifying lists

It is possible to change an element of a list dynamically simply by reassigning the value that the indexed variable points at. 

```python
shields = ['round', 'buckler', 'heater']
print(shields)
shields[0] = 'kite'
print(shields)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
['round', 'buckler', 'heater']
['kite', 'buckler', 'heater']
```

### Adding new items to a list 

Python lists have an inbuilt tool that allows you to append items to the end of a list. This tool is called `append(object)`. 

```python
shields = ['round', 'buckler', 'heater']
print(shields)
shields[0] = 'kite'
print(shields)
shields.append('targe')
print(shields)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
['round', 'buckler', 'heater']
['kite', 'buckler', 'heater']
['kite', 'buckler', 'heater', 'targe']
```

### Adding new items of the list at specific locations

Python also has tools to insert elements specifically where you want them. `insert(index, object)`. 

```python
shields = ['round', 'buckler', 'heater']
print(shields)
shields[0] = 'kite'
print(shields)
shields.append('targe')
print(shields)
shields.insert(0, 'pavise')
print(shields)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
['round', 'buckler', 'heater']
['kite', 'buckler', 'heater']
['kite', 'buckler', 'heater', 'targe']
['pavise', 'kite', 'buckler', 'heater', 'targe']
```

### Removing items from lists

Removing items from lists can be dangerous, so before you start doing this, think to yourself, do I really need to do this right now? 

To delete a specific element from a list, we can use the del command. 

```python
shields = ['round', 'buckler', 'heater']
print(shields)
shields[0] = 'kite'
print(shields)
shields.append('targe')
print(shields)
shields.insert(0, 'pavise')
print(shields)
del shields[0]
print(shields)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
['round', 'buckler', 'heater']
['kite', 'buckler', 'heater']
['kite', 'buckler', 'heater', 'targe']
['pavise', 'kite', 'buckler', 'heater', 'targe']
['kite', 'buckler', 'heater', 'targe']
```

### Removing the specific object

What happens if you don't know what element you want to remove? Python has a tool that will access the list and search it for you. 

```python
shields = ['round', 'buckler', 'heater']
print(shields)
shields[0] = 'kite'
print(shields)
shields.append('targe')
print(shields)
shields.insert(0, 'pavise')
print(shields)
del shields[0]
print(shields)
shields.remove('heater')
print(shields)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
['round', 'buckler', 'heater']
['kite', 'buckler', 'heater']
['kite', 'buckler', 'heater', 'targe']
['pavise', 'kite', 'buckler', 'heater', 'targe']
['kite', 'buckler', 'heater', 'targe']
['kite', 'buckler', 'targe']
```

### Sorting lists

Now we have been adding and removing items from our list for what seems like hours, how do we make our list all ordered and beautiful?

Python provides us with a tool that will attempt to sort lists. In the case of strings and numbers, this sorting is easy:

```python
shields = ['round', 'buckler', 'heater']
print(shields)
shields[0] = 'kite'
print(shields)
shields.append('targe')
print(shields)
shields.insert(0, 'pavise')
print(shields)
shields.sort()
print(shields)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
['round', 'buckler', 'heater']
['kite', 'buckler', 'heater']
['kite', 'buckler', 'heater', 'targe']
['pavise', 'kite', 'buckler', 'heater', 'targe']
['buckler', 'heater', 'kite', 'pavise', 'targe']
```

More complex data structures and objects can also be sorted, but we will cross that bridge when we come to it. 

### Iteration and lists

One of the most common tools for working through a lot of data are loops. Python comes with a number of loops but today we are going to work on for loops. 

You can think of for loops like this: `for each item in a list -> do something`

```python
knights = ['ada', 'bob', 'charlie']
for knight in knights: 
  print(knight)
```

```bash
foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
ada
bob
charlie
```

Once the for loop variable has been initialized, you can use the variable as you would any other variable. 

```python
knights = ['ada', 'bob', 'charlie']
for knight in knights: 
  print(knight)
  print(knight.title())
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
ada
Ada
bob
Bob
charlie
Charlie
```

### Creating lists dynamically

Technically speaking this is not a best practice in Python, but the ideology is broadly used in other programming languages.

Sometimes we find a need to dynamically create a list of numbers to use in our loop. The range function allows us to create a list of numbers.

```python
for value in range(1, 5):
  print(value)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
1
2
3
4
```

What's that range thing?

```python
print(list(range(1, 5)))
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
[1, 2, 3, 4]
```

It's a special function that helps us create a list. 

```python
squared_numbers = []
for value in range(1, 11):
  square = value**2
  squared_numbers.append(square)

print(squared_numbers)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Some neat tools for numbers in lists: 

```python
squared_numbers = []
for value in range(1, 11):
  square = value**2
  squared_numbers.append(square)

print(squared_numbers)
print(min(squared_numbers))
print(max(squared_numbers))
print(sum(squared_numbers))
```

```bash
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
1
100
385
```

### Conditions

Programming involves examining a set of conditions and deciding which action to take based off of those conditions. 

In python, we test conditions with the following statements. 

```python
if (condition1):
  #do_something
elif (condition2):
  #do_something_else
else: 
  #do_some_final_thing
```

```python
armours = ['gamberson', 'chainmail', 'plate', 'scale']
for armour in armours:
  if armour == "plate":
    print(armour.upper())
  else:
    print(armour.title())
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
Gamberson
Chainmail
PLATE
Scale
```

## Practice Question

### Practice 1

```python
'''Names: Store a list of the names of a few of your friends in a list called 
names. Print each person’s name by accessing each element in the list, one a 
time'''
```

### Practice 2

```python
'''Greetings: Start with the list from question 1, but instead of just printing 
each person’s name, print a message to them. The text of each message should be 
the same but each message should be personalised with the person’s name'''
```

### Practice 3

```python
'''Your own list: Think of your favourite modes of transportation, such as a 
motorcycle or car, and make a list that stores several examples. Use your list 
to print a series of statements about these items, such as “I would like to own 
a Honda motorcycle”. '''
```

### Practice 4

```python
'''
Guest list: If you could invite anybody from now or from history, to dinner, 
who would you invite? Make a list that includes at least three people you’d 
like to invite to dinner. Then use your list to print a message to each 
person, inviting them to dinner.
'''
```

### Practice 5

```python
'''
Changing Guest List: You just heard that one of your guests can’t make dinner, 
so you need to send out a new set of invitations. You’ll have to think of 
someone else to invite. 

Start with your program from Question 4. Add a print statement at the end of 
your program stating the name of the guest who can’t make it.

Modify your list, replacing the name of the guest who can’t make it with the 
name of the new person you are inviting.

Print a second set of invitation messages, one for each person who is still 
in your list.
'''
```

## Kevin's code


```python
#Fix my terrible code: 

thingos = ['thing', 'other_thing', "another_thing"]

for i in range(1, 10):
  print(thingo[i])
```

```python
#Fix my terrible code: 
different_thingos = [1, 2, 3, 4, 5]:
for i in different_thingos: 
  if i == 2:
    different_thingos.remove(different_thingos[i])
print(different_thingos)
```



## Challenge Question
