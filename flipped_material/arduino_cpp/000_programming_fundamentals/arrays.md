# Arrays 

### Learning Goals

*By the end of this module you should be able to answer the following:*

* What is an array? 
* How does an array relate to other data structures?
* What some common forms of array types are?

### Dictionary Corner

*To be able to answer a question, you need to be able to understand it. Pay special attention to Dictionary Corner because it arms you with the language to express yourself in this space.*

* Array: An array is a collection of variables that are accessed with an index number.

## Lesson

### What is an array:  

An array is a collection of elements of the same type placed in contiguous memory locations that can be individually referenced by using an index to a unique identifier.

Five values of type `int` can be declared as an array without having to declare five different variables (each with its own identifier).

For example, a five element integer array foo may be logically represented as;

|0|1|2|3|4|
|--|--|--|--|--|
|--|--|--|--|--|

Where each `--` represents an element of the array. In this case these values are of type int. These elements are numbered from 0 to 4, with 0 being the first while 4 being the last; In C++, the index of the first array element is always zero. As expected, an n array must be declared prior its use. A typical declaration for an array in C++ is:

```cpp
type name[#elements];
```
A more explicit example: 

```cpp
int foo[5];
```



### How to use arrays:

By default, arrays are left uninitialized. This means that none of its elements are set to any particular value; their contents are undetermined at the point the array is declared.

The initializer can even have no values, just the braces:

```cpp
int baz [5] = { }; 
```
This creates the following array: 
|0|1|2|3|4|
|--|--|--|--|--|
|0|0|0|0|0|

The number of values between braces {} shall not be greater than the number of elements in the array. For example, in the example above, foo was declared having 5 elements (as specified by the number enclosed in square brackets, []), and the braces {} contained exactly 5 values, one for each element. If declared with less, the remaining elements are set to their default values (which for fundamental types, means they are filled with zeroes). For example:

```cpp
int bar [5] = { 10, 20, 30 }; 
```
|0|1|2|3|4|
|--|--|--|--|--|
|10|20|30|0|0|

### Accessing arrays: 

The values of any of the elements in an array can be accessed just like the value of a regular variable of the same type. The syntax is:

```cpp
name[index];
```

Let's take the following array

```cpp
int foo[5] = {10, 20, 30, 40, 50};
```

We can access the first element like this: 

```cpp
Serial.println(foo[0]);
```

### How to iterate through arrays:

We can use for loops to iterate through arrays. Let's look at the following array: 

```cpp
char foo[4] = {'a', 'd', 'a', 'm'};
```

We can use the summative index (i) to point at the current index of the array. 

```cpp
for (int i = 0; i < sizeof(foo); i++){
    Serial.println(foo[i]);
}
```

## Practice and Challenges

### Questions

### Practice
