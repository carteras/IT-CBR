# Revision

## Objectives

* Properties
* classes/objects
* Inheritance and Polymorphism

## Properties

You are probably aware of class variables and using getters and setters to get and set them. 

```csharp
class Student
{
  private int _age;

  public int GetAge()
  {
    return _age;
  }

  public void SetAge(int age)
  {
    _age = age;
  }
}
```

There is nothing wrong with this, but there is a better way. Properties.

 In C#, a Property represents a private field with bound Get and/or Set methods.

```csharp
class Student
{
  public int Age { get; set; }
}
```

What happens if you want to do something fancy with a getter or setter? 

```csharp
class Tiger
{
    private int _age;

    public int Age
    {
        get
        {
            return _age;
        }

        set
        {
            if (value > 0) // Check for the valid age
            {
                _age = value;
            }
        }
    }

    public static void Main()
    {
        var tiger = new Tiger();

        tiger.Age = 2;                 // Ok, valid age
        tiger.Age = -2;                // Invalid value, age was NOT assigned

        Console.WriteLine(tiger.Age);  // Outputs 2
    }
}
```

## classes/objects

Object-oriented Programming (OOP) is one of the most effective approaches to writing software. 

The concept of OOP is relatively easy. Programmers define a standard blueprint for similar objects and then instantiate them when they need one. When you write a class, you define the general behaviour for that object.  

Understanding object-oriented programming will help you break up complex problems into smaller, easier to solve chunks. This process will help you think logically about problems both in and beyond programming. 

You can model almost any concept with classes. Let's start with Dogs. 

This class doesn't represent just one dog, but it represents all dogs. What do we know about most pet dogs? They all have names, ages, and they know some common commands

```csharp
using System;

namespace HelloObjects
{

    public abstract class Animal {
        public string Name { get; set; }
        public string Sound { get; set; }

        public Animal(string name, string sound) {
            Name = name;
            Sound = sound;
        }
        public abstract string MakeNoise();
    }

    public class Dog : Animal {

        public Dog(string name) : base(name, sound) { 
            string sound = "Woof";
        }
        public override string MakeNoise() {
            return $"{Name} goes {Sound}";
        }
    }

    public class Cat : Animal {
        public Cat(string name) : base(name, sound){
            string sound = "Mew";
        }

        public override string MakeNoise() {
            return $"{Name} goes {Sound} and it love/hates you.";
        }
    }
    public class Program {
        public static void Main(string[] args) {
            Dog d = new Dog("Sam");
            Console.WriteLine(d.MakeNoise());
            System.Diagnostics.Trace.WriteLine(d.MakeNoise());
        }
    }
}
```

## Inheritance Polymorphism and Polymorphic Behaviour

```csharp
using System;

namespace Revision2021S2 {

    public abstract class Animal {
        public string Name { get; set; }
        public string Sound { get; set; }

        public Animal(string name, string sound) {
            Name = name;
            Sound = sound;
        }
        public abstract string MakeNoise();
    }

    public class Dog : Animal {

        public Dog(string name, string sound) : base(name, sound) { }
        public override string MakeNoise() {
            return $"{Name} goes {Sound}";
        }
    }
    public class Program {
        public static void Main(string[] args) {
            Dog d = new Dog("Sam", "Woof");
            Console.WriteLine(d.MakeNoise());
            System.Diagnostics.Trace.WriteLine(d.MakeNoise());
        }
    }
}
```

## Challenges

Using the code below create a solution that allows for 100 cars to race. 

* Cars need a different accel
* Cars need a different reliability

* Start with objects/classes

Notes about cars: 

* Sedans
  * accel 1.0
  * reliability 1.0
  * max speed 10
* SUVs
  * accel 0.75
  * reliability 1.25
  * max speed 15
* Bogan Ute
  * accel 1.5
  * reliability 0.5
  * max speed 17.5

```csharp
using System;

namespace Revision2021S2 {
    public class Program {
        public static void Main(string[] args) {
            Random rnd = new Random();

            int raceDistance = 100000;

            double carAccel1 = 0.75;
            double carSpeed1 = 0;
            double carDistance1 = 0;
            double carReliability1 = 1.25;
            double maxSpeed1 = 15;

            double carAccel2 = 1.0;
            double carSpeed2 = 0;
            double carDistance2 = 0;
            double carReliability2 = 1.0;
            double maxSpeed2 = 10;

            bool racing = true;

            while (racing) {
                if (carReliability1 > rnd.Next(0, 2)) {
                    carSpeed1 += carAccel1;
                }
                if (carReliability2 > rnd.Next(0, 2)) {
                    carSpeed2 += carAccel2;
                }
                carDistance1 += carSpeed1;
                carDistance2 += carSpeed2;

                if (carDistance1 >= raceDistance) {
                    racing = false;
                }
                if (carDistance2 >= raceDistance) {
                    racing = false;
                }
            }

            // Make some code to decide the winner!!!
            
            
        }
    }
}

```