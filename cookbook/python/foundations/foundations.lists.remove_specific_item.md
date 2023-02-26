# How to remove specific objects from a list? 

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* How can you remove a specific item in a list without knowing it's index?


## Concepts

What happens if you don't know what element you want to remove? Python has a tool that will access the list and search it for you. 

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
shields.remove('heater')
print(shields)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
['round', 'buckler', 'heater']
['kite', 'buckler', 'heater']
['kite', 'buckler', 'heater', 'targe']
['pavise', 'kite', 'buckler', 'heater', 'targe']
['kite', 'buckler', 'heater', 'targe']
['kite', 'buckler', 'targe']
```


## Practice Question

```python
''' given the following lists remove the targe from each one'''

shields1 = ['pavise', 'kite', 'buckler', 'heater', 'targe']
shields2 = ['pavise', 'kite', 'targe','buckler', 'targe', 'heater']
shields3 = ['pavise', 'kite', 'targe','buckler', 'heater', 'targe']
shields4 = ['pavise', 'targe','kite', 'buckler', 'heater', 'targe']
shields5 = ['targe','pavise', 'kite', 'buckler', 'heater']

# Your code goes here
# Your code goes here
# Your code goes here
# Your code goes here
# Your code goes here

print(shields1)
print(shields2)
print(shields3)
print(shields4)
print(shields5)

```