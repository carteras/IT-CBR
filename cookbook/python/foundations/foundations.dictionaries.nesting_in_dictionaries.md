# Putting dictionaries inside dictionaries?

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* What?


## Concepts

Did you know that you can put a dictionary inside another dictionary? That's right! When you do this, each thing you put inside the dictionary is also a dictionary.

Someone may want to put a dictionary inside another dictionary when they need to store more information for a particular key. For example, let's say you are making a program for a library and you want to store information about different books. You could create a dictionary where each key is the name of a book and its value is another dictionary containing information about the book, such as the author, the genre, and the publication date. This way, you can access all the information related to a particular book easily by using its key.

```python
programmers = {
  'alovela': {'given_name': 'ada','family_name': 'lovelace','location': 'London'},
  'ghopper': {'given_name': 'grace', 'family_name': 'hopper','location': 'virginia',}
}

for programmer in programmers:
  print(f"username: {programmer.upper()}")
  for details in programmers[programmer]:
    print(f" - {details}: {programmers[programmer][details].title()}")
```

Example output:

```shell
username: ALOVELA
 - given_name: Ada
 - family_name: Lovelace
 - location: London
username: GHOPPER
 - given_name: Grace
 - family_name: Hopper
 - location: Virginia
 ```

## Practice Question

Using the following code as a starting point. Create a program that makes a dictionary of dictionary. Each dictionary key consists of the first letter of their given name followed by the first six letters of their family name.

```python
programmers = {}

while True:
  user_input = input("Enter your given name, family name, and location.") 
  if user_input == "q": break
  # your code goes here
  # your code goes here
  # your code goes here
  # your code goes here
  # your code goes here
  # your code goes here

for programmer in programmers:
  print(f"username: {programmer.upper()}")
  for details in programmers[programmer]:
    print(f" - {details}: {programmers[programmer][details].title()}")
```
