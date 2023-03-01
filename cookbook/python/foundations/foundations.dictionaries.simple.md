# What is a dictionary?

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* What is a dictionary in python? 
* What is a key?
* What is a value?
* What relationship does a key have to the value?
* How what are two simple ways of building dictionaries?
* How to print dictionaries to standard console.

## Concepts

In Python, dictionaries let you connect related information by storing them as pairs of keys and values. If you give a dictionary a key, it will give you the value that's connected to it. You can look through all the pairs, keys, or values in a dictionary too.

To make a dictionary in Python, you can use curly braces. To connect a key to its value, you use a colon. You can make more than one connection by using commas between each key-value pair.

```python
my_dict = {'key': 'value'}
print(my_dict)
```

```shell
{'key': 'value'}
```

```python
my_dict = {}
my_dict['key'] = 'value'
```

```shell
{'key': 'value'}
```

```python
dog = {'breed': 'Golden Retriever', 'age': 3}
print(dog)
```

```shell
{'breed': 'Golden Retriever', 'age': 3}
```

```python
bird = {}
bird['species'] = 'Parakeet'
bird['age'] = 2
print(bird)
```

```shell
{'species': 'Parakeet', 'age': 2}
```

## Practice Question

Create a dictionary of a family pet (or your ideal family pet) that consists of the following keys:

* name
* species
* age