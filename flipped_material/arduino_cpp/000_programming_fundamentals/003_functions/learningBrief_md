# Functions

## Objectives

* Know how to identify specific processes that a Control System must accomplish and understand how to implement that in a system
* Know how to map identified processes to their desired input and output and understand how to implement that in logic 
* Know how to create simple functions that relate the input, process, and output identified in Control Systems

### Dictionary Corner:

Nobody would doubt that having strong literacy skills is important for almost every part of life. The same is true in technical subjects: sharing a common technical literacy makes it easier for professionals to talk to each other. 

* In the world of programming a microcontroller, what is a process? 
* Why is consensus so important while designing systems? 



## Functions

What is a function? 

Being able to segment your code into manageable chunks allows a programmer to create module pieces of code that perform different tasks and then return to the area of code from when the function was “called”. The typical cases for creating functions are: 

* You have a lot of code in the main the loop and you need to move it elsewhere
* You are repeating the same code over and over again. 

We’ve already seen a bunch of functions in use. 
* void setup(){}
* void loop(){}
* pinMode(pin, INPUT|OUTPUT);
* digitalWrite(pin, HIGH|LOW);
* digitalRead(pin);

![](2021-10-10-13-20-07.png)

There is a lot of similarity between functions and variables both have: 
A data type; and
A name (or a label)

However, functions also have input that they can manipulate and turn into a range of different outputs. 

In the example above, the function myMultiplyFunction accepts two variables, x and y, and returns their product. Here is an example: 


![](2021-10-10-13-20-33.png)

Can we turn this into a function (or maybe even a series of functions)? 
* In this case, the input is simply going to be a function call (although we could abstract this). So, we don’t need any input. 
* In more complex versions of this, we would change the global state of the system at the end but for our example, we can ignore that. 
* We can write all of the logic in that function.


![](2021-10-10-13-21-12.png)

![](2021-10-10-13-21-51.png)

This turns into a lot of code so I will just move to the end: 

![](2021-10-10-13-22-35.png)


We can also refactor this code further with more functions: 

![](2021-10-10-13-23-03.png)

## Challenges

Your challenge is to create and modify the circuit and code given here and refactor it so it uses functions to clean up your main function. 