# Modifying lists?

> Python lists allow
> Elements accessed by index,
> Modify with ease.

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* How you can access lists via their index.
* How do you modify a list element at a given index.

## Concepts

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

## Practice Question

```python
''' using the following list, change sabre to cutlass '''
swords = ['mortuary', 'arming', 'long', 'sabre']
print(swords)
# your code goes here
print(swords)
```
