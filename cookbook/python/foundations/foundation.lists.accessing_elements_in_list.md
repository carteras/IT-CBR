# How do we access elements in a list?

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* Are lists ordered?
* How do you access an element in a list

## Concepts

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

## Practice Questions

```python
'''given the following list, print the second and third items. Print the second in title case and the third in upper case.
'''
swords = ['mortuary', 'arming', 'long', 'sabre']

print(f"second element in title case is: {}")
print(f"third element in upper case is: {}")

```

```python
''' using a for loop, loop through every item in the list and print it in upper case. Use the following output as a guide: 
'The best sword is ****'
'''
swords = ['mortuary', 'arming', 'long', 'sabre']
```
