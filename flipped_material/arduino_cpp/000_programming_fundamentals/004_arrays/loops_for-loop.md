# for loops 

### Learning Goals

*By the end of this module you should be able to answer the following:*

* What is a loop?
* What are for loops? 
* How do we tell for loops how to start and stop? 
* How do we increment the summative index?
* How are loops used with arrays?

### Dictionary Corner

*To be able to answer a question, you need to be able to understand it. Pay special attention to Dictionary Corner because it arms you with the language to express yourself in this space.*

* for loop - A for loop is a repetition control structure that allows you to efficiently write a loop that needs to execute a specific number of times.
* initialise step - The initialise step is executed first, and only once. This step allows you to declare and initialize any loop control variables. You are not required to put a statement here, as long as a semicolon appears.
* condition - If it is true, the body of the loop is executed. If it is false, the body of the loop does not execute and flow of control jumps to the next statement just after the for loop.
* increment statement - what happens after the body of the loop has been executed. 

## For loops 

### Starting and stopping for loops

In steps:

* sets the variable `i` as the type of integer and assigns it to 0 
* sets the operating condition to only work while i is less than 10. 

```cpp
for (int i = 0; i < 10; i++){
    Serial.println(i);
}
```

Prints out a sequence from 0 -> 9
```cpp
for (int i = 10; i > 0; i--){
    Serial.println(i);
}
```

Will print 10 -> 1

### Accessing an array. 

For loops are often used to access an array of things. Consider the following code: 

```cpp
Serial.begin(9600);

char foo[4] = {'a', 'd', 'a', 'm'};

for (int i = 0; i < 4; i++){
    Serial.println(foo[i]);
}
```

We can use the index feature of the array to access individual elements of the array. The incrementing nature of the for loop means that we can set the start of the for loop to start at the start of the array and we can iterate through the entire array. 

### How can we know the size of an array after we make it? 

It's a bit of a code smell to have to continually write the size of the array out. It's very easy to make mistakes this way. 

Consider this solution of setting a maximum size variable. 

```cpp
Serial.begin(9600);
int size = 4;
char foo[size] = {'a', 'd', 'a', 'm'};
Serial.println(size);
for (int i = 0; i < size; i++){
    Serial.println(foo[i]);
}
```

## Practice and Challenges

#### Practice

##### Practice 1

Create a for loop that counts from 0 to 100.

##### Practice 2

Create a for loop that counts from 99 to 0.

##### Practice 3

Create a for loop that counts from 0 to 100 but only prints even numbers. 
 

##### Practice 4

```cpp
Serial.begin(9600);
String foo = "programming is bonza";
for (int i = 0; i < foo.length(); i++){
    
}
```

Hey, what's that fancy `.length()`? :)

##### Practice 5

Toby wants to assign pins 3 to 8 as input and then pins 9 to 13 as output. Do this with two for loops! 


##### Practice 6

Timmy has written this code and it doesn't work. Help Timmy solve his problem by fixing his bugs. 

```cpp
Serial.begin(9400);
int size = 9;
int foo[size] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
for (int i = 0; i < foo.size(); i++){
    Serial.println(foo(i));
}
```