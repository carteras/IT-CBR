# Topic

What are objects, how do they work, why do I care?

## TL;DR

In object-oriented programming, we categorise things as classes. Classes are things that represent things or situations. Programmers can then instantiate classes to create objects based off of those classes. Programmers can then use these classes/objects to chunk the complexity into management parts.

**original author:** [carteras](https://github.com/carteras)

<!-- add a new author mark if you updated this -->

## Topics covered

"At the end of this recipe, you will be able to answer the following questions or solve the following problems"

<!-- why should people expect to be able to do or know after doing this recipe -->

* What came before classes?
* Why do I care about Objects?
* What is a class?
* What is an object?
* How do you define a class? 
* How do you instantiate a class to become an object?
* How can you use classes to reduce the complexity of your code?

### Things you'll need to know before you start this

<!-- what should they know before learning it -->

* Foundation Python

### Third party resources

<!-- Are there other locations where they can find this information? -->

* resource
* resource
* resource

## Topics

### Introduction

<!-- Introduce the topic, what is it, how does it work, include pictures -->

Programming gets very complicated, very quickly. Imagine that we are going to create a system that connects to a group of point of sales systems. Each of the point of sales systems was made by a different manufacture and different rules for how to access the data on the system and how that data is stored. Now, imagine that you want to classify, transform, and sort that data into a system that you can generate reports from. How do you even start to break this problem up?

### What came before objects and object oriented code?

Prior to Object Oriented Programming paradigm, programmers used to construct proto-objects. In fact, we've done this before. Let's think back to a program we wrote at the beginning of last semester. 

```python
from statistics import mean, median, mode
from pathlib import Path
from inspect import currentframe, getframeinfo

this_filename = getframeinfo(currentframe()).filename
here = Path(this_filename).resolve().parent

names = []
scores = []

with open(here/"test_results.txt") as test_results:
    for line in test_results:
        line = line.strip()
        name, score = line.split(':')
        score = int(score)
        names.append(name)
        scores.append(score)

highest_score = max(scores)
first_highest = names[scores.index(highest_score)]
print(first_highest, highest_score)
```

Storing the names and scores in two lists is a form of proto object. We are capturing the overall state of a thousand different users in a kind of data structure. 

Other languages allowed us to create what we will call a structure and make a list of them. 

```c
struct Score {
  char name[50];
  int score;
};

int main(){
  struct Scores scores[1000];
  for (int i = 0; i < 1000; i++){
    printf("Enter a name:");
    scanf("%s",&scores[i].name); 
    printf("Enter a score:");
    scanf("%d",&scores[i].score);  
  }
  printf("Student %s got a score of %d.\n", scores[489].name, scores[489].score)
}
```

This process allows us to connect both the name and the score together.

### Why do I care about Objects?

So, with structures we can create our own custom datatype for the data we are working with. In this case, we created a Score DataType that contains both a name and a score. 

What if we wanted to model something bigger? What if we wanted to model a zoo? Zoos are full of animals, can we use structures to define an entire zoo? 

Maybe, but it start to get complicated

```c
struct Animal {
  char name[50];
  char species[50];
  char sound[50];
};

void makeSound(struct Animal a){
  printf("%s the % goes %s\n", a.name, a.species, a.sound)
}

int main(){
  struct Animal animals;
  for (int i = 0; i < 10; i++){
    printf("Enter a name:");
    scanf("%s",&animals[i].name); 
    printf("Enter a species:");
    scanf("%d",&animals[i].species);
    printf("Enter a sound they make: ")
    scanf("%d",&animals[i].sound);
  }
  makeSound(a[4]);
}
```


At some point, Computer Scientists started to feel constrained with this form of `functional programming`. Sometimes animals had shared functionality other times they didn't, more importantly, sometimes the verbs (the functions) needed to have the same name for different things. Something needed to change. 

### What is a class?

A class is a data type that incorporates both attributes and functionality together. 

```python
class Cat:
    def __init__(self):
        '''
        The initiliser is a standard piece of code for classes. 
        It initliases the object with any specific variables it needs to have. 

        The self keyword represents this objects internal state. 
        '''
        print("This is a cat")

c = Cat()
```

```python
class Cat:
    def __init__(self, name):
        self.name = name
        print(f"This is a cat, it's name is {self.name}")

c = Cat("Kaylee")
```

```python
class Cat:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        print(f"This is a cat, it's name is {self.name}, it goes {self.sound}")

c = Cat("Kaylee", "mew")
```

### How can you use classes to reduce the complexity of your code?

```python
class Cat:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} goes {self.sound}!"

c = Cat("Kaylee", "mew")
print(c.make_sound())
```

```python
class Cat:
    def __init__(self, name, sound, hungry = False):
        self.name = name
        self.sound = sound
        self.hungry = hungry

    def make_sound(self):
        return f"{self.name} goes {self.sound}!"

    def check_hunger(self):
        if self.hungry:
            return f"{self.name} makes urgent {self.sound} sounds!"
        return f"{self.name} flicks their tail in annoyance!"


c = Cat("Kaylee", "mew")
print(c.make_sound())
print(c.check_hunger())
c.hungry = True
print(c.check_hunger())
```

```python
import names
from random import choice, randint

class Cat:
    def __init__(self, name, sound, hungry = False):
        self.name = name
        self.sound = sound
        self.hungry = hungry

    def make_sound(self):
        return f"{self.name} goes {self.sound}!"

    def check_hunger(self):
        if self.hungry:
            return f"{self.name} makes urgent {self.sound} sounds!"
        return f"{self.name} flicks their tail in annoyance!"

sounds = ["mew", "meow", 'MEOW']
cats = []
for _ in range(10):
    cats.append(Cat(names.get_first_name(), choice(sounds)))

while True:
    c = choice(cats)
    rnd = randint(1, 10)
    if rnd < 3:
        print(c.make_sound())
    elif rnd < 6:
        print(c.check_hunger())
    else:
        c.hungry = not c.hungry

```


## Practice Questions

<!-- Provide some basic worked examples that let people follow your worked examples. If it's a library, don't forget to tell people how to install it -->

```python
class Cat:
  pass

cats = []
c1 = Cat("Kaylee", 12, 'calico', 'tortoiseshell', 'f')
c2 = Cat("Sylvester", 11, 'jerk', 'black', 'm')
cats.append(c1)
cats.append(c2)

print(f"I have {len(cats)} cats and their names are ", end='')
for i in range(len(cats)): 
  if i < len(cats)-1:
    print(f" {cats[i].name}, ", end="")
  else:
    print(f" and {cats[i].name}.")

for cat in cats:
  print(f'{cat.name} is {cat.age} and {cat.sex} is a {cat.cat_type} with pretty {cat.markings} coat')
```


## Challenge

<!-- Make up a challenge question which asks people to use all of their knowledge they just learnt (and maybe some prior learning) to solve -->

You are challenged to make two classes: A racetrack and racecar

### race cars 

* Have a driver (name)
* have a car number
* Have an acceleration between 0.5 and 1.5
* have a maximum speed between 5 and 10
* cars can not accelerate beyond their maximum speed
* Each tick, cars accelerate until they reach their max speed

### A racetrack 

* Can have 10 cars on the track
* Is 1000 units long
* each tick prints the current position of all cars by units 
* each tick, the race track has a 1 in 100 chance of causing an obstacle which makes a car slow down to 50%
* the game keeps playing until someone wins
* report who came first
* stop the race