# How do you modify a value in a dictionary?

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* How to modify a value in a dictionary using an existing key. 

## Concepts

You can change the information in a dictionary. If you want to change the value that's already there for a key, you can just give the dictionary's name and the key inside square brackets, and then put in the new value.

```python
creature = {'colour': 'red', 'score': 8}
print(creature)
# Change the creature's colour and score value.
creature['colour'] = 'blue'
creature['score'] = 15
print(creature)
```

```shell
{'colour': 'green', 'points': 5}
{'colour': 'yellow', 'points': 10}
```

This code defines a dictionary named creature with a colour key that has a value of 'red' and a score key with a value of 8. The code then prints the contents of the dictionary using the print() function. The code then modifies the values associated with the colour and score keys using the assignment operator =. Finally, the modified dictionary is printed again to show the changes.

## Practice Question

```python
animal = {"name": "Spot", "species": "dog", "age": 3}

# Change the age of the animal here


# Print the updated animal dictionary
print(animal)
```

### Instructions

You are given a dictionary called animal with the keys "name", "species", and "age".

Your task is to change the age of the animal to twice its current value.
Make sure to update the value of the "age" key in the animal dictionary.
Finally, print out the updated animal dictionary to see if your code works correctly.

### Example output

```shell
{"name": "Spot", "species": "dog", "age": 6}
```

### Hints

* Start by defining a dictionary with some key-value pairs.
* Use the print() function to display the dictionary.
* Use the keys of the dictionary to change the corresponding values.
* Use the print() function again to display the updated dictionary and check your changes.
* Remember to use the correct syntax for changing the value associated with a key in a dictionary.
* If you get stuck, try breaking the problem down into smaller steps and tackle them one at a time
