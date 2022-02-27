# Joining Strings

## Topics covered

"At the end of this learning brief, you will be able to answer the following questions"

* How do I join a bunch of characters together into a string? 


## Learning Resources

* [python docs: str.join(iterable)](https://docs.python.org/3/library/stdtypes.html#str.join)

## Topics

### joining lists of characters into strings

Sometimes it is easier to work in lists rather than strings. Especially when we are trying different combinations of characters. 

Python has a special command that allows us to join a list of characters together called `join()`

```python
letters = ['a', 'b', 'c']
print(letters)
print(''.join(letters))
print(' '.join(letters))
print('_'.join(letters))
```

```text
['a', 'b', 'c']
abc
a b c
a_b_c
```