# Date time (draft)

## Topics covered

"At the end of this learning brief, you will be able to answer the following questions"

* How to access python's datetime module


## Learning Resources

* 

## Topics

### Measuring time

Sometimes we want to know how long different techniques take. Python has a good understanding of time through the `datetime library

```python
from datetime import datetime 
a = datetime.datetime.now()
x = 1
for i in range(1, 10000):
  x = x * x+1
delta_time = datetime.datetime.now() - a
print(f'The answer was {x} and we found it in {delta_time}')
```