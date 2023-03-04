# Storing lists in dictionaries ?

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* How do you store a list in a dictionary?
* How do you access a list stored in a dictionary?

## Concepts

In Python, if you want to connect many pieces of information to one key, you can put a list inside a dictionary. This lets you store more than one value with each key.

```python
pets_owned = {
  'bob': ['cat', 'dog'],
  'samantha': ['fish', 'dog'],
  'josh': ['cat', 'bird'],
  'olivia': ['fish', 'bird'],
  'jacob': ['cat', 'fish']
}

for name in pets_owned:
  print(f"{name}")
  for pet in pets_owned[name]:
    print(f" - {pet}")
```

## Practice Question

```python
'''
Print the contents of the following gear
Use the example output below this code

'''
fantasy_fighter_gear = {
  'weapons': ['longsword', 'broadsword', 'arquebus', 'crossbow', 'halberd', 'pike', 'lance', 'mace', 'war hammer', 'flail', 'morning star', 'battle axe', 'war pick', 'short sword', 'dagger', 'falchion', 'scimitar', 'war scythe', 'war club', 'morningstar flail', 'claymore', 'rapier', 'sabre', 'estoc', 'bardiche', 'glaive', 'voulge', 'scythe', 'katana', 'naginata', 'zweihander'],
  'armour' : ['mail armor', 'plate armor', 'lamellar armor', 'brigandine armor', 'scale armor', 'leather armor', 'cuir bouilli armor', 'linothorax armor', 'kikko armor', 'horned helmet', 'nasal helmet', 'bascinet helmet', 'great helm', 'barbute helmet', 'sallet helmet', 'armet helmet', 'greaves', 'poleyns', 'couters', 'vambraces', 'gauntlets', 'mittens', 'bracers', 'cuisses', 'jambeaux', 'sabatons', 'gambeson armor', 'aketon armor', 'harness armor', 'brigandine armor', 'o-yoroi']
}

# Your code goes here
# Your code goes here
# Your code goes here
# Your code goes here
```

Your output should look like this:

```shell
weapons
 - longsword
 - broadsword
 - arquebus
 - crossbow
 - halberd
 - pike
 - lance
 - mace
 - war hammer
 - flail
 - morning star
 - battle axe
 - war pick
 - short sword
 - dagger
 - falchion
 - scimitar
 - war scythe
 - war club
 - morningstar flail
 - claymore
 - rapier
 - sabre
 - estoc
 - bardiche
 - glaive
 - voulge
 - scythe
 - katana
 - naginata
 - zweihander
armour
 - mail armor
 - plate armor
 - lamellar armor
 - brigandine armor
 - scale armor
 - leather armor
 - cuir bouilli armor
 - linothorax armor
 - kikko armor
 - horned helmet
 - nasal helmet
 - bascinet helmet
 - great helm
 - barbute helmet
 - sallet helmet
 - armet helmet
 - greaves
 - poleyns
 - couters
 - vambraces
 - gauntlets
 - mittens
 - bracers
 - cuisses
 - jambeaux
 - sabatons
 - gambeson armor
 - aketon armor
 - harness armor
 - brigandine armor
 - o-yoroi
```