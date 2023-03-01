# How do you access values in dictionaries?

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* How to return the value from a dictionary using only a key

## Concepts

If you have a dictionary in Python and want to get a certain piece of information, you can type the name of the dictionary, then put the key you're looking for in square brackets. But be careful! If the key isn't in the dictionary, you'll get an error.

There's another way to get information called get(). This won't give you an error if the key isn't there, it'll just give you nothing. If you want to make sure you get something, you can tell get() what to give you if the key is missing.

```python
car = {'make': 'Honda', 'model': 'Civic', 'year': 2022}
print(car['make'])
print(car['year'])
```

```shell
Honda
2022
```

With a `.get()` example: 

```python
monster = {'fur': 'purple'}
monster_fur = monster.get('fur')
monster_horns = monster.get('horns', 2)
monster_eyes = monster.get('eyes')
print(monster_fur)
print(monster_horns)
print(monster_eyes)
```

## Practice Question

Suppose you have a dictionary of students with their test scores:

```python
def get_score(name, students):
    ...

students = {'Alice': [95], 'Bob': [87], 'Charlie': [92], 'Dave': [84]}


if __name__ == "__main__"():
    for name in students:
        print(f"{name} received {get_score(name, students)}")
```

Complete the function get_score(name) that takes a student's name as an argument and returns their score. The function should return None if the given name is not in the dictionary of students.

Note: This question tests your ability to use dictionaries with list values to look up values by keys, and to handle cases where a key is not found. You may assume that each student's name appears only once in the dictionary.
