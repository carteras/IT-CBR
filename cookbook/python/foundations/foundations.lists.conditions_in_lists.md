# Making decisions with lists and iteration? 

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* How do you make decisions while iterating through lists?


## Concepts

Programming involves examining a set of conditions and deciding which action to take based off of those conditions. 

In python, we test conditions with the following statements. 

```python
if (condition1):
  #do_something
elif (condition2):
  #do_something_else
else: 
  #do_some_final_thing
```

```python
armours = ['gamberson', 'chainmail', 'plate', 'scale']
for armour in armours:
  if armour == "plate":
    print(armour.upper())
  else:
    print(armour.title())
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
Gamberson
Chainmail
PLATE
Scale
```


## Practice Question

```python
''' Iterate through the following list and create a set of conditions to change the way we print them out
For example: 

* Shields that end in e should be in upper case
* Shields that end in r should be in title case
* Shields that are are 5 letters long should be reversed
'''

shields = ['pavise', 'kite', 'buckler', 'heater', 'targe']
```
