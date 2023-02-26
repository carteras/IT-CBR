# How do you remove items from lists? 

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* How do you delete an item at a specific index from a list


## Concepts

Removing items from lists can be dangerous, so before you start doing this, think to yourself, do I really need to do this right now?

To delete a specific element from a list, we can use the del command.

```python
shields = ['round', 'buckler', 'heater']
print(shields)
shields[0] = 'kite'
print(shields)
shields.append('targe')
print(shields)
shields.insert(0, 'pavise')
print(shields)
del shields[0]
print(shields)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
['round', 'buckler', 'heater']
['kite', 'buckler', 'heater']
['kite', 'buckler', 'heater', 'targe']
['pavise', 'kite', 'buckler', 'heater', 'targe']
['kite', 'buckler', 'heater', 'targe']
```

## Practice Question

```python
'''
Given the following list, remove the kite and heater shields
'''
shields = ['pavise', 'kite', 'buckler', 'heater', 'targe']
print(shields)
# your code goes here
# your code goes here
print(shields)
```
