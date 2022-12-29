# Itertools

## Topics covered

"At the end of this learning brief, you will be able to answer the following questions"

* Topical Question
* Topical Question
* Topical Question

## Learning Resources

* [Python docs: Itertools](https://docs.python.org/3/library/itertools.html)

## Topics

### itertools

itertools is a module that provides a range of functions to manage looping very efficiently. 

### PIN number cracking

```python
import itertools
numbers = '0123456789'
secret = "000044"
for c in itertools.product(numbers, repeat=6):
  print(c)
  if secret == ''.join(c):
    print(''.join(c))
    break
```

