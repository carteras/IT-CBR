# How do you create simple lists dynamically?

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* How can you generate a list of numbers?


## Concepts

Technically speaking this is not a best practice in Python, but the ideology is broadly used in other programming languages.

Sometimes we find a need to dynamically create a list of numbers to use in our loop. The range function allows us to create a list of numbers.

```python
for value in range(1, 5):
  print(value)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
1
2
3
4
```

What's that range thing?

```python
print(list(range(1, 5)))
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
[1, 2, 3, 4]
```

It's a special function that helps us create a list. 

```python
squared_numbers = []
for value in range(1, 11):
  square = value**2
  squared_numbers.append(square)

print(squared_numbers)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Some neat tools for numbers in lists: 

```python
squared_numbers = []
for value in range(1, 11):
  square = value**2
  squared_numbers.append(square)

print(squared_numbers)
print(min(squared_numbers))
print(max(squared_numbers))
print(sum(squared_numbers))
```

```bash
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
1
100
385
```

## Practice Question

```python
'''
Using a for loop and range, generate a triangle that looks like this: 

* 
**
***
****
*****


'''
```
