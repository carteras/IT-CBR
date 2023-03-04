# How do you remove a key-value pair?

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* How do you remove a key and it's value in a dictionary?


## Concepts

You can take away anything you don't need from a dictionary. To do this, you use a special word called "del" and the name of the dictionary. Then, you put the name of the thing you want to take away inside square brackets. This will remove it from the dictionary.

```python
pet_owners = {
  'bob': 'cat',
  'samantha': 'dog',
  'josh': 'fish',
  'olivia': 'parrot',
  'jacob': 'dog'
}
print(pet_owners)
del pet_owners['jacob']
print(pet_owners)
```

## Practice Question

From the following data structure, remove the location from both inner dictionaries

```python

programmers = {
  'agarcia': {'given_name': 'ada','family_name': 'lovelace','location': 'London'},
  'lhopper': {'given_name': 'grace', 'family_name': 'hopper','location': 'virginia',}
}

# Your code goes here
# Your code goes here

# this just prints out all of the data about programmers
for programmer in programmers:
  print(f"username: {programmer.upper()}")
  for details in programmers[programmer]:
    print(f" - {details}: {programmers[programmer][details].title()}")

```

Your output should look like this: 

```shell
username: AGARCIA
 - given_name: Ada
 - family_name: Lovelace
username: LHOPPER
 - given_name: Grace
 - family_name: Hopper
 ```
 