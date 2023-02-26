# Using lists!

One of the best ways of learning is to start with a challenge and learn the steps of solving that challenge.

* They provide clear learning objects for the learner: learners are given a clear goal to achieve. 
* When linked with scaffolded training, learners don't have to worry about going down the wrong path
* Promotes active learning 
* Fosters problem solving skills

## Prerequisite learning

To solve the following challenge, you may need to complete the following cookbooks:

* [Cookbook: Introduction to lists](../../cookbook/python/foundations/foundations.introductions.md)
* [Cookbook: Accessing elements in a list](../../cookbook/python/foundations/foundations.lists.accessing_elements_in_list.md))
* [Cookbook: Modifying lists](../../cookbook/python/foundations/foundations.lists.modifying_lists.md)
* [Cookbook: Adding new items to a list](../../cookbook/python/foundations/foundations.lists.add_item_at_index.md)
* [Cookbook: Adding new items of the list at specific locations](../../cookbook/python/foundations/foundations.lists.add_item_at_index.md)
* [Cookbook: Removing items from lists](../../cookbook/python/foundations/foundations.lists.remove_item.md)
* [Cookbook: Removing specific objects from lists](../../cookbook/python/foundations/foundations.lists.remove_specific_item.md)
* [Cookbook: Sorting lists](../../cookbook/python/foundations/foundations.lists.sorting.md)
* [Cookbook: Iteration and lists](../../cookbook/python/foundations/foundations.lists.iterating.md)
* [Cookbook: Creating lists of numbers dynamically](../../cookbook/python/foundations/foundations.lists.dynamic_list_generation.md)
* [Cookbook: Using conditions in lists](../../cookbook/python/foundations/foundations.lists.conditions_in_lists.md)

## Other links that might be useful

* Google for Education: [Lists methods](https://developers.google.com/edu/python/lists)  
* Python-Textbook: [selection control statements](https://python-textbok.readthedocs.io/en/1.0/Selection_Control_Statements.html)

## Chad's code


```python
# Fix my terrible code: 

thingos = ['thing', 'other_thing', "another_thing"]

for i in range(1, 10):
  print(thingo[i])
```

```python
# Fix my terrible code: 
different_thingos = [1, 2, 3, 4, 5]:
for i in different_thingos: 
  if i == 2:
    different_thingos.remove(different_thingos[i])
print(different_thingos)
```

## Challenge Question

```python
''' From the following list, find the only non-unique word
'''

words = ['pupas', 'rewet', 'where', 'upped', 'peter', 'aumil', 'photo', 'azyms', 'kydst', 'reifs', 'quoys', 'theft', 'regia', 'poral', 'miles', 'quare', 'lynes', 'qualy', 'weeke', 'pudgy', 'serve', 'muton', 'kadis', 'agree', 'pleas', 'satyr', 'cotes', 'shark', 'weeis', 'moile', 'gnarl', 'whins', 'cloke', 'siler', 'doggy', 'soyuz', 'dandy', 'crepy', 'moria', 'rarks', 'belli', 'waled', 'goody', 'spiel', 'zaire', 'waffs', 'eruct', 'pownd', 'octet', 'embar', 'stirk', 'dorse', 'acned', 'rotty', 'lense', 'roule', 'jumar', 'kinda', 'rekey', 'tragu', 'draco', 'cardi', 'keema', 'mirrs', 'kyudo', 'yeeds', 'potes', 'japer', 'evegs', 'diary', 'disas', 'sorra', 'plain', 'yonny', 'alkos', 'mante', 'chout', 'metol', 'symar', 'fards', 'dukka', 'murva', 'recon', 'takht', 'twyer', 'gawks', 'hunky', 'spelk', 'fibro', 'pohed', 'perky', 'readd', 'muntu', 'tiros', 'takhi', 'vexes', 'cezve', 'derth', 'gompa', 'ocrea', 'lores', 'spait', 'malmy', 'graze', 'dobes', 'villa', 'ysame', 'inapt', 'nonic', 'sitka', 'aboon', 'clash', 'rotls', 'psych', 'abacs', 'bunts', 'heald', 'trunk', 'ships', 'wembs', 'khafs', 'feast', 'smith', 'commo', 'grens', 'nelly', 'stean', 'ahent', 'rakia', 'wiled', 'aloft', 'abrim', 'plumy', 'sadis', 'alien', 'blite', 'filks', 'womyn', 'vexes', 'forza', 'calmy', 'altho', 'huies', 'happi', 'molvi', 'drive', 'gyver', 'gites', 'algas', 'mesic', 'swads', 'memic', 'campi', 'ranns', 'pores', 'inwit', 'demit', 'matts', 'voces', 'wasts', 'dreed', 'hammy', 'mauvy', 'helot', 'peepe', 'sarir', 'shoud', 'ioras', 'shule', 'arith', 'katis', 'rejas', 'jakie', 'xolos', 'oaker', 'renne', 'agars', 'rings', 'clank', 'bonce', 'combe', 'lader', 'ergon', 'rowts', 'wavey', 'angas', 'civil', 'dente', 'petar', 'vrous', 'woosh', 'mihas', 'tuxes', 'horme', 'rudes', 'grays', 'mooks', 'calps', 'flamy', 'mardy', 'mudra', 'aguna', 'speld', 'jalap', 'apism', 'shako', 'scuta', 'jetes', 'yites', 'lindy', 'ebbet', 'binit', 'nodal', 'tabus', 'sagum', 'croci', 'unfix', 'kawau', 'dhals', 'pubis', 'maqui', 'brast', 'mivvy', 'sekos', 'yates', 'clunk', 'loner', 'yewen', 'lewis', 'rebuy', 'kivas', 'taxer', 'dinlo', 'sokes', 'pesos', 'maill', 'slorm', 'raddy', 'wolds', 'poppy', 'scant', 'forel', 'sluts', 'glory', 'aahed', 'ajiva', 'ommel', 'slink', 'kreef', 'throb', 'vibey', 'bitts', 'grant', 'dunce', 'ebike', 'fight', 'clips', 'golly', 'scram', 'swags', 'deare', 'sitch', 'towsy', 'jurel', 'deair', 'paler', 'puses', 'ouped', 'stots', 'sedum', 'pixie', 'natto', 'joual', 'routh', 'renin', 'xebec', 'guile', 'soyas', 'pheer', 'yabas', 'galed', 'races', 'lesbo', 'bides', 'lance', 'ngaka', 'venge', 'rasas', 'rykes', 'aread', 'putas', 'curia', 'alpha', 'edged', 'spirt', 'virgo', 'girns', 'trams', 'binal', 'punks', 'forby', 'seine', 'iodic', 'swash', 'lises', 'duads', 'hibas', 'derma', 'cauda', 'knish', 'kojis', 'rucks', 'artsy', 'risus', 'gambs', 'mvule', 'quims', 'facia', 'sheen', 'armil', 'gursh', 'dagga', 'nucin', 'limma', 'deign', 'yoghs', 'unzip', 'karks', 'acute', 'lubed', 'byres', 'hokas', 'swarm', 'hangi', 'clack', 'tunds', 'tacet', 'sonne', 'femic', 'leery', 'gulfy', 'tided', 'usnea', 'povos', 'nkosi', 'funny', 'ahead', 'beigy', 'dazer', 'pecia', 'yowed', 'mowed', 'rains', 'oriel', 'whipt', 'duply', 'until', 'votes', 'nanty', 'arias', 'devot', 'gayly', 'jougs', 'drums', 'tawie', 'plouk', 'bafta', 'pryan', 'drone', 'keaki', 'cools', 'ouzos', 'daynt', 'zinke', 'peeps', 'pheon', 'erugo', 'lurry', 'waded', 'boats', 'toged', 'meaty', 'knaur', 'vouge', 'humph', 'rines', 'boody', 'tinty', 'khaya', 'fossa', 'reefs', 'prime', 'phooh', 'mells', 'skirr', 'chows', 'hijab', 'falsy', 'misky', 'sorex', 'stude', 'cocky', 'burry', 'talon', 'doest', 'ezine', 'ratos', 'orixa', 'avise', 'drink', 'panni', 'ycond', 'faena', 'cusps', 'wilds', 'dares', 'unsex', 'mogue', 'fillo', 'pusle', 'fixed', 'stunk', 'clour', 'nisus', 'swizz', 'peach', 'lymes', 'weedy', 'wizes', 'roomy', 'retia', 'debur', 'wispy', 'prune', 'kapow', 'flawy', 'judge', 'dural', 'anear', 'merge', 'techy', 'verve', 'whity', 'spats', 'subak', 'wider', 'links', 'purer', 'sapan', 'brick', 'canes', 'duroc', 'milly', 'super', 'lehrs', 'ouzel', 'lotah', 'weils', 'oaten', 'kacks', 'crwth', 'scats', 'spree', 'aking', 'afore', 'sport', 'hoary', 'kawed', 'rokes', 'bands', 'knule', 'wizzo', 'catch', 'pinto', 'vints', 'pikas', 'loams', 'huhus', 'pirls', 'fitly', 'these', 'toeas', 'fytte', 'chads', 'refis', 'cunny', 'ureas', 'anise', 'nudie', 'decay', 'score', 'nalas', 'brame', 'lomas', 'medii', 'bices', 'hiked', 'flame', 'munts', 'rages']

# Your code goes here
# Your code goes here
# Your code goes here
# Your code goes here
# Your code goes here
# Your code goes here
```

```shell
>>> D:\github\IT-CBR>python -u "d:\github\secretnerdbusiness\foo.py"
duplicate word detected: *****
```