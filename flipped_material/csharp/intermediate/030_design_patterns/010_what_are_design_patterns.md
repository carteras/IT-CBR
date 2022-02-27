# Design Patterns 

### Learning Goals

*By the end of this module you should be able to answer the following:*

* What is a design pattern? 
* Why would software engineers use design patterns

### Dictionary Corner

*To be able to answer a question, you need to be able to answer it. Pay special attention to Dictionary Corner because it arms you with the language to express yourself in this space.*

* OOP - Object Oriented Programming
* Polymorphism - the provision of a single interface to entities of different types
* Design Patter - a best use case for solving common problems. 

## Design Patterns

In software engineering, a software design pattern is a general, reusable solution to a commonly occurring problem within a given context in software design. It is not a finished design that can be transformed directly into source or machine code. Rather, it is a description or template for how to solve a problem that can be used in many different situations. Design patterns are formalized best practices that the programmer can use to solve common problems when designing an application or system.

### History 

Design Patterns are inherited from architecture and the metaphor was translated into software design by Kent Beck and Ward Cunningham in 1987. 

Design Patterns take the process of solving common problems with best practice approaches. In general, these best practices consist of: 

* Programming to an interface not an implementation
* Composition over inheritance 

They also developed categories for Design Patterns: 

* Creational - patterns that create desired objects programmatically.
* Structural - patterns that define how classes should be designed
* Behavioural - patterns that define communication between objects
  


### Program to an interface, not implementation

What does that mean? 

Programming to an interface means that we decouple the implementation of a concept from the use of a concept. We do this with abstractions. 

For example, we might have customers who use a range of payment gateways (credit cards, paypal, bitcoin). Programming to an interface means that we make a library or API which handles all of the particular gateways, and then make a common interface that works for all of them. 

### Composition over Inheritance

Composition over Inheritance is the principal that classes should achieve polymorphic behaviour by their composition rather than defining a whole class. 

For example, instead of Greyhounds inheriting from Dog, you'd make Greyhounds inherit legs, mouths, bodies, and etc. 

More on this later. 

