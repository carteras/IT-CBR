# How do you add an item to a list at a specific index?

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* How do you add data to a specific element in a list?

## Concepts

Python also has tools to insert elements specifically where you want them. `insert(index, object)`. 

```python
shields = ['round', 'buckler', 'heater']
print(shields)
shields[0] = 'kite'
print(shields)
shields.append('targe')
print(shields)
shields.insert(0, 'pavise')
print(shields)
```

```bash
[foo@bar code]$ /usr/bin/python /home/foo/nerdstuff/code/IT-CBR/.foo/foo.py
['round', 'buckler', 'heater']
['kite', 'buckler', 'heater']
['kite', 'buckler', 'heater', 'targe']
['pavise', 'kite', 'buckler', 'heater', 'targe']
```

## Practice Question

```python
''' given the following list, insert the roman shield 'scutum' between buckler and heater shields'
'''
shields = ['pavise', 'kite', 'buckler', 'heater', 'targe']
```
