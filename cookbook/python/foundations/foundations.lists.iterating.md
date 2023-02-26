# How can we iterate through lists?

> Iterating through Python's list,
> With a loop that won't be missed,
> You explore each item with glee,
> Until you reach the end with ease,
> And find what you need, no need to insist.

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* How to iterate through lists in python

## Concepts

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

## Practice Question

```python
''' 
Using the following list, iterate through each one and print it using the following text guide: 
'**** is my favourate sword!
Make sure that you put your sword in title text!
'''

swords = ['mortuary', 'arming', 'long', 'sabre']

# your code goes here
# your code goes here
# your code goes here
```
