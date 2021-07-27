# Make a copy for your own work! 

# Object-oriented programming

Object-oriented Programming (OOP) is one of the most effective approaches to writing software. 

The concept of OOP is relatively easy. Programmers define a standard blueprint for similar objects and then instantiate them when they need one. When you write a class, you define the general behaviour for that object.  

Understanding object-oriented programming will help you break up complex problems into smaller, easier to solve chunks. This process will help you think logically about problems both in and beyond programming. 

Object-oriented programming comes with its own challenges, some of which we will encounter over the next few weeks, but first, let's see them in action. 

## You will learn

* Know what classes are
* Know what objects are
* Know the key terminology relating to classes
* Understand how to construct a class
* Understand how to instantiate an object from a class
* Use classes and objects to solve complex problems. 

### What is a class? 

### What are objects?

### Creating Dogs
You can model almost any concept with classes. Let's start with Dogs. 

This class doesn't represent just one dog, but it represents all dogs. What do we know about most pet dogs? They all have names, ages, and they know some common commands

```csharp
using System;

namespace HelloObjects
{

    class Dog
    {
        private string _name;

        public string Name { get; set; }

        public Dog(string name) {
            this.Name = name;
        }

        public string bark()
        {
            return $"{this.Name} barks. Woof Woof!";
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Dog d = new Dog("Sam");
            Console.WriteLine(d.bark());
        }
    }
}
```

Now, there is a lot going on there. So, let's break it up, and have a look at what is going on.

```csharp
public Dog(string name) {
    this.Name = name;
}    
```
This is a Constructor. It builds the individual object by assigning different state variables around. 

```csharp
private string _name;
```

This is a private class variable that stores some state variable. 

```csharp
public string Name { get; set; }
```

This is some c# magic that handles getting and setting of variables for us. 

#### Practice

Add some methods to the dog class which allow them to preform tricks. Then modify your base class to write that input out. 

```csharp
public string come(){}
public string rollOver(){}
public string sit(){}
```

### Working with classes and objects
Using lists, let's create  multiple dogs. Modify your program with the following. 

```csharp
static void Main(string[] args)
class Program
{
    static List<Dog> dogs;
    static void Main(string[] args)
    {
        dogs = new List<Dog>();
        dogs.Add(new Dog("Sam"));
        dogs.Add(new Dog("Max"));
        dogs.Add(new Dog("Ranger"));

        foreach (Dog dog in dogs)
        {
            Console.WriteLine(dog.bark());
        }
    }
}
```

### Interactive Classes 
It is possible to interact with classes beyond just getting information out of them. Modify your code with the changes made below. 

```csharp
namespace HelloObjects
{
    class Dog
    {
        public string Name { get; set; }
        public int NumTreats { get; set; }

        public Dog(string name) {
            this.Name = name;
            this.NumTreats = 0;
        }

        public string bark()
        {
            return $"{this.Name} barks. Woof Woof!";
        }

        public void eatTreat()
        {
            this.NumTreats++;
        }
    }
    class Program
    {
        static List<Dog> dogs;
        static void Main(string[] args)
        {
            dogs = new List<Dog>();
            dogs.Add(new Dog("Sam"));
            dogs.Add(new Dog("Max"));
            dogs.Add(new Dog("Ranger"));

            foreach (Dog dog in dogs)
            {
                Console.WriteLine(dog.bark());
            }

            dogs[0].eatTreat();
            Console.WriteLine(dogs[0].NumTreats);
        }
    }
}
```

## Challenges 

### Dictionary Corner

### Circles 

Create a class that takes it's radius as a parameter and then create three methods that describes that circle: 

```csharp
getCircumference() -> the circumference of the circle (float)
getArea() -> the area of the circle (float)
describe() -> returns a string "The circle has the radius R and has the circumference of C. With R and C being getters. 
```
### Calculator
Create methods for the Calculator class that can do the following:

* Add two numbers.
* Subtract two numbers.
* Multiply two numbers.
* Divide two numbers.

```csharp
calculator = Calculator()
calculator.add(10, 5) ➞ 15
calculator.subtract(10, 5) ➞ 5
calculator.multiply(10, 5) ➞ 50
calculator.divide(10, 5) ➞ 2
```

### DogPark

Using your Dog class. Create a dog park. The desired output will look something like this: 

```
Daisy runs about! Arf! ARF!
Bella runs about! Yip! YIP!
Sam runs about! Yap! YAP!
```

Bonus gloats if you can dynamically create dogs with random names and bark sounds 


### Advanced Challenge 

OOP Walk the plank

In this challenge you are to make two classes: a Plank, and a Pirate.

* The plank has 7 locations
* All pirates start at location 0.
* Each turn Pirates are prodded to move.
* If a pirate is prodded they decide if they move forwards or backwards.
* Pirates can not loop around to the far end of the plank
* If a pirate gets to the other end they are removed from the plank
* After all pirates have moved the plank reports how many pirates are at each point.
* The program will end when there are no more pirates to prod
* I highly encourage pirate themed statements from the pirates when they move or fall off the plank.