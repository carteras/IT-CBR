# Dictionaries

## Topics covered

"At the end of this learning brief, you will be able to answer the following questions"

* What is a dictionary?
* How do you add data to a dictionary?
* How do you retrieve data from a dictionary?
* How do you iterate through a dictionary?

## Learning Resources

* [Dictionaries](https://www.programiz.com/python-programming/dictionary)
* [Nested Dictionaries](https://www.programiz.com/python-programming/nested-dictionary)

## Topics

### Python Programming: Dictionaries

A dictionary is a key-pair collection which is ordered by when the elements are inserted. 

You might be thinking to yourself "wait ... what?".  Imagine an actual dictionary. You look up a word (the key) and find the definition (the value). 

```
awesome adjective

awe·​some | \ ˈȯ-səm  \
Definition of awesome
1. inspiring awe
    * an awesome task/responsibility
    * a place of awesome beauty
    * binformal : TERRIFIC, EXTRAORDINARY
    * had an awesome time at the concert
2. expressive of awe
    * awesome tribute
```

### A simple dictionary

```python
#short and sharp
foo = {'key' : 'value'}

#if you have a lot of elements
bar = {
  'key1' : "value1",
  'key2' : 'value2'
}

print(foo['key'])
print(bar['key2'])

```
As written above a dictionary in python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value that it is associated with. 

Keys are generally strings or maybe numbers. In general, the best practice is to make them identifiable to increase readability, i.e., strings. 

Values can be anything, numbers, strings, objects, lists, or even other dictionaries.

### Working with dictionaries

To get a value from a key, simply give the name of the dictionary and the name of the key inside a set of square brackets.

```python
adam = {'hair': 'ginger'}

print(adam['hair'])
```

You can have a practically unlimited number of key-value pairs. For example: 

```python
adam = {
  'hair':'ginger',
  'eyes':'hazel',
  'height':'tall',
  'profession':'nerdwrangler',
  'given_name':'adam'
}

print('Teachers, what is your profession!')
print(f"{adam['given_name']}: is a {adam['profession']}")
```

### Adding new key-value pairs

Dictionaries are dynamic in nature. This means that you can add new key-value pairs at any time. 

```python
adam = {
  'hair':'ginger',
  'eyes':'hazel',
  'height':'tall',
  'profession':'nerdwrangler',
  'given_name':'adam'
}

print(adam)
adam['family_name'] = 'carter
print(adam)
```

### Modifying a value 
The values of a dictionary are also dynamic. 
```python
adam = {
  'hair':'ginger',
  'eyes':'hazel',
  'height':'tall',
  'profession':'nerdwrangler',
  'given_name':'adam'
}
print(adam['hair'])
adam['hair'] = 'ginger striped with silver'
print(adam['hair'])
```

### Removing a key-value pair
Like lists, we can remove a key-value pair with the `del` command
```python
adam = {
  'hair':'ginger',
  'eyes':'hazel',
  'height':'tall',
  'profession':'nerdwrangler',
  'given_name':'adam'
}

print(adam)
del adam['hair']
print(adam)
```

### Iterating through a dictionary

```python
adam = {
  'hair':'ginger',
  'eyes':'hazel',
  'height':'tall',
  'profession':'nerdwrangler',
  'given_name':'adam'
}

for key in adam:
  print(f'This is the key {key}, and with it I can get the value {adam[key]})
```

## Practice Questions

### Practice Question 1

Use a dictionary to store information about a person you know. Store their given name, family name, age, and the city that they live. You should have keys such as `given_name`. Print each piece of information in your dictionary. 

### Practice Question 2

Use a dictionary to store people's lucky numbers. The data should be stored as key:value with the key being their given_name and the value being their lucky number. 

Iterate through this dictionary and print the output so it says:

`f"{key}'s lucky number is {value}"`

### Practice Question 3

A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.

* Think of five programming words you’ve learned about in the previous
weeks. Use these words as the keys in your glossary, and store their
meanings as values.

* Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.

## Mastery Questions

### Mastery Question 1

Extend practice question 1 by creating a dictionary of dictionaries. Each key in the parent dictionary consists of a key:value of key="given_name_family_name" and value = the entire dictionary above. 

Iterate through each key and print all of their details in the following format. 

f`{key}: {family_name}, {given_name} - lucky number is {lucky_number}`

e.g.,:

```text
annemory: Emory, Ann - lucky number is 20
forresthoffman: Hoffman, Forrest - lucky number is 22
emmahubbs: Hubbs, Emma - lucky number is 68
alvinhaney: Haney, Alvin - lucky number is 4
donnawhitson: Whitson, Donna - lucky number is 99
jacobmorales: Morales, Jacob - lucky number is 10
soniawarman: Warman, Sonia - lucky number is 49
larrypaules: Paules, Larry - lucky number is 6
hueycastle: Castle, Huey - lucky number is 57
stanleyfreeman: Freeman, Stanley - lucky number is 71
```
