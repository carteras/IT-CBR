# How do test questions work?  

## Learning Goals

*By the end of this module you should be able to answer the following:*

* How does the test file work? 
* What is a unit test?
* How do you know if you should have passed the unit test? 


## Context

Unit tests are automated tests that are designed to verify the functionality of individual units or modules of source code. These tests are typically written by developers to ensure that their code is functioning correctly and to catch any bugs or errors before the code is deployed to production.

### Example: 


Put the following code into your IDE: 

```python

def my_sum(a, b):
    return a + b

if __name__ == "__main__":
    assert(my_sum(1, 1)) == 2
```

If you execute this, nothing happens. 

Now, change the my_sum function: 


```python
def my_sum(a, b):
    return a - b

if __name__ == "__main__":
    assert(my_sum(1, 1)) == 2
```

If you execute this, it produces the following exception: 

```shell
Traceback (most recent call last):
  File "/home/foo/nerdstuff/code/IT-CBR/.foo/foo.py", line 5, in <module>
    assert(my_sum(1, 1)) == 2
AssertionError
```

## Practice Questions


### Practice:

## Fluff about find out

So, you've learnt lots of things so far today. I challenge you to use your imagination and try and find some things that you feel you might be able to do, but weren't necessarily taught.

Because it's our first week, I am happy to give you some hints to start you off, but go nuts. 


## Bug hunt

Kevin has written some code and it doesn't work. What's wrong with it?
