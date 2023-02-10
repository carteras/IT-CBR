# Lists

## Learning Goals

*By the end of this module you should be able to answer the following:*

* Know what Lists are and what common syntax exists to manipulate them
* Gain a broad understanding of how to use lists to solve foundation problems.
* Know what conditions are. 
* Understand how to use simple conditions to make decisions

##Conceptual Links:

Google for Education: [Lists methods](https://developers.google.com/edu/python/lists)  
Python-Textbook: [selection control statements](https://python-textbok.readthedocs.io/en/1.0/Selection_Control_Statements.html)

##What is a list? 

A list is a collection of items. Lists can be made from anything, the letters of the alphabet, the names of your classmates, the words in a secret cipher, the ages of your family. Lists can even be made up of different things. 

Think of them a bit like a set of draws, the top draw might be for underwear and socks, the second draw might be for shirts, the third draw might be for pants. 

Because lists generally hold multiple things it's best to make the name of your list a plural. words, names, bicycles, are all good descriptive names for lists. 

In python, a list is indicated by the use of square brackets `[]`. 

Here is an example: 

```python
swords = ['mortuary', 'arming', 'long', 'sabre']
print(swords)
```

Here, I create a list of strings with the name of various types of swords. I then assign that list of strings to a variable called swords. 

### Accessing elements in a list 

Lists are ordered collections. This means that they remain in the order that you left them in. By doing this, it becomes possible to access elements in the list if you know it's position or index. 

To access an element in a list, we use the lists variable name followed by the index position of the item in square brackets. 

For example, using my list of sword names, I can access the first sword name. 

```python
print(swords[0])
```
It's important to note here, that indexes start at 0, not 1. This is because the number line starts at 0, not 1. 

00, 01, 02, 03, 04, 05, 06, 07, 08, 09  
10, 11, 12, 13, 14, 15, 16, 17, 18, ,19

and so on...

This use of an element in a list can be used like any other variable. Below, I have an f-string that is using the index position of the first sword.   



```python
first_sword = f'My first sword was a {swords[0].title()}.'
print(first_sword)
```

### Modifying lists

It is possible to change an element of a list dynamically simply by reassigning the value that the indexed variable points at. 

```python
shields = ['round', 'buckler', 'heater']
print(shields)
shields[0] = 'kite'
print(shields)
```

###Adding new items to a list 

Python lists have an inbuilt tool that allows you to append items to the end of a list. This tool is called `append(object)`. 

```python
shield.append('targe')
print(shield)
```

### Adding new items of the list at specific locations

Python also has tools to insert elements specifically where you want them. `insert(index, object)`. 

```python
shield.insert(0, 'pavise')
print(shield)
```
### Removing items from lists

Removing items from lists can be dangerous, so before you start doing this, think to yourself, do I really need to do this right now? 

To delete a specific element from a list, we can use the del command. 

```python
del shield[0]
print(shield)
```

What happens if you don't know what element you want to remove? Python has a tool that will access the list and search it for you. 

```python
shield.remove('pavise')
print(shield)
```

### Sorting lists

Now we have been adding and removing items from our list for what seems like hours, how do we make our list all ordered and beautiful? 

Python provides us with a tool that will attempt to sort lists. In the case of strings and numbers, this sorting is easy: 

```python
shield.sort()
print(shield)
```

More complex data structures and objects can also be sorted, but we will cross that bridge when we come to it. 

### Iterating through lists

One of the most common tools for working through a lot of data are loops. Python comes with a number of loops but today we are going to work on for loops. 

You can think of for loops like this: `for each item in a list -> do something`

```python
knights = ['alice', 'bob', 'charlie']
for knight in knights: # a common technique is to use the single term for the variable
  print(knight)
```

Once the for loop variable has been initialised, you can use the variable as 

---

you would any other variable. 

```python
for knight in knights:
  print(knight.title())
```

This use/reuse of a the loop variable is true for multiple uses in the same iteration. 

```python
for knight in knights:
  print(f'{knight.title()}, that was a great fight!')
  print(f"I can't wait to see your next bought {knight.title()}")
```

Once a loop has finished it re-joins the natural procedure of the program. 

```python
for knight in knights:
  print(f'{knight.title()}, that was a great fight!')
  print(f"I can't wait to see your next bought {knight.title()}")
print("Thank you, everyone! That what a great tournament!")
```

### Creating lists dynamically

Technically speaking this is not a best practice in Python, but the ideology is broadly used in other programming languages. 

Sometimes we find a need to dynamically create a list of numbers to use in our loop. The range function allows us to create a list of numbers. 

```python
for value in range(1, 5):
  print(value)
```

```python
numbers = list(range(1, 5))
print(numbers)
```

```python
squared_numbers = []
for value in range(1, 11):
  square = value**2
  squared_numbers.append(square)

print(squared_numbers)
```

Some neat tools for numbers in lists: 

```python
print(min(squared_numbers))
print(max(squared_numbers))
print(sum(squared_numbers))
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

###So many equal signs

One of the things about programming is that we end up with a lot of different operators that use the equals sign `=` for something. E.g., 

`=, ==, >=, <=, !=, +=, -=, *-, /=, %=` 

Visually, they are fairly straight forewords. However, verbally, this becomes much more complicated; especially with `=, and ==`. 

To combat this, I use some verbal cues: 

`=` means 'is assigned' or 'gets the value of something' so I call it assign or gets

'==' means we are testing the logical condition equivalence of the statement. So I say equivalent to. 

### Test for equivalence

To test for equivalence we use `==`

```python
armour = 'plate'
print(armour == 'plate', armour == 'scale')
```

### Testing for not equivalent

To test for not equivalent we use `!=`

```python
print(armour != "plate", armour != "scale")
```

### Other conditions

We can also test some other common conditions such as greater than or equal to, less than or equal to, etc. 

```python
age1 = 16
print(age1 >= 15 and age1 <= 18)
print(age1 <15 or age1 < 18)
```

### Testing to see if something is in a list

There are some other conditions tests we can use. For example, we can test to see if a object is in a list with the `in` operator. 

```python
toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in toppings)
```

Likewise, we can test to see if an object is not in a list

```python
print('apple' not in toppings)
```

### Selection Statements (if/elif/else)

We can string `if, elif, else` statements together to test potential conditions. 

```python
topping = 'pineapple'
if topping == 'mushrooms':
  print("YES! Mushrooms!")
elif topping == 'onions':
  print("NO! Not onions!")
elif toppings == "pineapple":
  print("Ah, the fruit that tries to eat you!")
else:
  print("What topping is this?")
```

### Selection statements in loops

We can also embed selection statements inside loops to create branching logic within the loop. 

```python
requested_toppings = ['mushrooms', 'capsicum', 'extra cheese']
for topping in requested_toppings:
  if topping == 'capsicum':
    print("Sorry, we are out of capsicum at the moment")
  else: 
    print(f'Adding {topping} to your pizza')
print("making your pizza now!")
```

## Code

*It is important to practice code and challenge our brain in new ways. Do all of the problems below, including the example problems. They will make you a better programmer.*

### Example Problems

*Example problems are best if you code them up yourself and store them. Don't just copy and paste, code them in and make them work. If you are really smart about it, you'll remake them slightly differently to really establish your learning.*

### Practice Problems

*Practice questions are essential to mastering a skill. Often, you will be asked to do things you haven't exactly done yet, or not at all. Be challenged by it and see if you can get google, the person next to you, or the teacher, to help before you stop working.*

### Practice 1

```python
'''Names: Store a list of the names of a few of your friends in a list called 
names. Print each person’s name by accessing each element in the list, one a 
time'''


```

#### Practice 2

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

#### Fix my terrible code:

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

```python
#Fix my terrible code
foo = True

if foo = True:
  print("success")
else: 
  print("what?")
```