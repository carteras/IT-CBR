# How do we make decisions in Arduino C?

In Arduino C, conditions are used to make decisions in code by evaluating if some statement is true or false. 

## Learning Goals

*By the end of this recipe you should be able to answer or use the following:*

* ==
* !=
* <
* \>
* <=
* \>=
* ||
* &&
* What a boolean value is
* What branching logic is
* How to use if to decide to enter a branch
* How to use if-else to decide to enter one branch or another
* How to use the if-else-if-if chain to use a all capturing state for a branch





## Concepts

### Comparison Operators

These include "==" (equal to), "!=" (not equal to), "<" (less than), ">" (greater than), "<=" (less than or equal to), and ">=" (greater than or equal to).

```cpp
int a = 5;

if (a == 5){
    // do something if a is equivalent to 5
}
```

```cpp
if a = 5;

if (a != 5){
    // do something if a is not equivalent to 5
}
```

```cpp
if a = 5;

if (a < 5){
    // if a is less than 5 do something
}

```

#### Multiple comparisons

It is possible to have multiple comparisons in an if statements. 

We can use the logical operators `||` for ored and `&&` for anded statements. 

```cpp 
int a = 5;
int b = 100;

if (a == 5 || a > 50){
    // if a is 5 or greater than 50 do something
}
```

```cpp
int a = 45;
int b = 15;

if (a % 5 == 0 && a % 3 == 0){
    // if a is equally divisible by 5 and 3 do something
}

```

### Boolean values 

There are only two boolean values: `true` and `false`. Sometimes this is represented by `1` and `0`. These are used to represent the truth value of an expression

### The if statement

The `if` statement is used to execute a block of code only if a certain condition is met. The syntax is: 

```cpp

if (condition){
    // branch code
}

```

### If else 

The if-else statement is used to execute one block of code if a condition is true or another block of code if it is false.

```cpp
if (condition){
    // then do this
} else {
    // do something else 
}

```

### The if-else-if-else statement

if, else-if, else staement is used to execute different blocks of code based on multiple conditions. 

```cpp
if (condition1){
    // do this
} else if (condition2){
    // instead do this
} else {
    // otherwise do this
}
```

### Boolean logic 

Boolean logic in programming refers to the use of data that is only true or false. The operations and (&&), or (||), or not (!) are used to represent and manipulate the truth values. These truth values are used in conditions to make decisions in code. 

In C boolean data can be either true or false or 1 and 0. 


The and operator: The and operator is used to evaluate two conditions and return True if both conditions are True, otherwise it returns False. The syntax is:

```bash
condition1 && condition2
```

The or operator: The or operator is used to evaluate two conditions and return True if at least one of the conditions is True, otherwise it returns False. The syntax is:

```bash
condition1 || condition2
```

The not operator: The not operator is used to invert a truth value. If the condition is True, not returns False, and if the condition is False, not returns True. The syntax is:

```bash
!condition
```

```cpp
x = 5
y = 10

Serial.println(x > 2 &&  y < 20) # True
Serial.println(x < 2 || y > 20) # False
Serial.println(!x > 2) # False
```


