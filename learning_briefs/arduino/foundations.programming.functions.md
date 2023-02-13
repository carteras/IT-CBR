# Functions

## Objectives

* Know how to identify specific processes that a Control System must accomplish and understand how to implement that in a system
* Know how to map identified processes to their desired input and output and understand how to implement that in logic 
* Know how to create simple functions that relate the input, process, and output identified in Control Systems

### Dictionary Corner:

Nobody would doubt that having strong literacy skills is important for almost every part of life. The same is true in technical subjects: sharing a common technical literacy makes it easier for professionals to talk to each other. 

* In the world of programming a microcontroller, what is a process? 
* Why is consensus so important while designing systems? 



---
title: Arduino Functions
revealOptions: 
    transition: 'fade'
---

## Arduino Functions

> Functions break down code,  
> Reusability's key,  
> Efficiency gained.  

<!-- .slide: style="text-align: left;"> -->

---

## By the end of today you will

* Know what functions are
* Know why functions return data types
* Gain a better understanding on data types
* Know why functions can accept parameters 
* Understand how to create a simple function
* Create your own function

<!-- .slide: style="text-align: left;"> -->

---

## What is a function

So far we've been writing all of our instructions in 3 spaces: 

* global space 
* setup function
* loop function

Chances are your loop function is starting to get insane

<!-- .slide: style="text-align: left;"> -->

---
## Insane main loops

```cpp [|1-3|5-7|9-10|12-14|17|19-20|23-34|38-39|40-44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|59|60|61|62|63|64|65|66|67|68|69|70|71|72|73|74|75|76|77|78|79|80|81|82|83|84|85|86|87|88|89|90|91|92|93|94]
// define sensors 
#define btn_left 3
#define btn_right 2

// define actuators
#define LED_LOW 8
#define LED_HIGH 13

// defining global delay time
#define DELAY_TIME 500

// define states
#define SCROLL_LEFT 1
#define SCROLL_RIGHT 2
#define STOP 0

int state = STOP;

int leftButton;
int rightButton;


void setup()
{
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(btn_left, INPUT);
  pinMode(btn_right, INPUT);
  Serial.begin(9600);
}

void loop()
{
  leftButton = digitalRead(btn_left);
  rightButton = digitalRead(btn_right);
  if (leftButton) {
    state = SCROLL_LEFT;
  } else if (rightButton){
    state = SCROLL_RIGHT;
  }
  Serial.println(state);
  if (state == SCROLL_RIGHT){
    digitalWrite(13, HIGH);
    delay(DELAY_TIME);
    digitalWrite(13, LOW);
    digitalWrite(12, HIGH);
    delay(DELAY_TIME);
    digitalWrite(12, LOW);
    digitalWrite(11, HIGH);
    delay(DELAY_TIME);
    digitalWrite(10, LOW);
    digitalWrite(10, HIGH);
    delay(DELAY_TIME);
    digitalWrite(10, LOW);
    digitalWrite(9, HIGH);
    delay(DELAY_TIME);
    digitalWrite(9, LOW);
    digitalWrite(8, HIGH);
    delay(DELAY_TIME); 
    digitalWrite(8, LOW);
    state = STOP;
  }else if (state == SCROLL_RIGHT){
    digitalWrite(8, HIGH);
    delay(DELAY_TIME);
    digitalWrite(8, LOW);
    digitalWrite(9, HIGH);
    delay(DELAY_TIME);
    digitalWrite(10, LOW);
    digitalWrite(10, HIGH);
    delay(DELAY_TIME);
    digitalWrite(10, LOW);
    digitalWrite(11, HIGH);
    delay(DELAY_TIME);
    digitalWrite(11, LOW);
    digitalWrite(12, HIGH);
    delay(DELAY_TIME);
    digitalWrite(12, LOW);
    digitalWrite(13, HIGH);
    delay(DELAY_TIME); 
    digitalWrite(13, LOW);
    state = STOP;
  } else if (state == STOP){
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    digitalWrite(10, LOW);
    digitalWrite(9, LOW);
    digitalWrite(8, LOW);
    state = STOP;
  }
}
```

<!-- .slide: style="text-align: left;"> -->

---
## Wow that was a lot of code

Did anybody see the bugs?

Well there are some 

<!-- .slide: style="text-align: left;"> -->

---
## Debugging that mess is hard

And programmers are lazy. 

<!-- .slide: style="text-align: left;"> -->

---
## Wouldn't it be cool of Arduino C could help us simply? 

Luckily, it can. 

<!-- .slide: style="text-align: left;"> -->

---
## Functions

Functions consist of four parts: 

* the function label
* input parameters that the function can use
* a return type
* whatever the function returns

<!-- .slide: style="text-align: left;"> -->

---
## Function label  

the function label is the name of the function. 

Consider the following example:

```cpp
int myAdd(int a, int b){
    return a + b
}
```

The function label is `myAdd`


<!-- .slide: style="text-align: left;"> -->

---
## Function parameters  

Functions can take input from elsewhere. Consider the following function. 

```cpp
int myAdd(int a, int b){
    return a + b
}
```

This function accepts two integer numbers `a` and `b`

<!-- .slide: style="text-align: left;"> -->

---
## Function returns 

Again, consider the following chunk of code:

```cpp
int myAdd(int a, int b){
    return a + b
}
```

This function returns the sum of a and b here `return a + b`

<!-- .slide: style="text-align: left;"> -->

---
## Return Types

We need to tell the compiler what functions will return. We can consider that code block again: 

```cpp
int myAdd(int a, int b){
    return a + b
}
```

This function returns an `int`

<!-- .slide: style="text-align: left;"> -->

---
## What does void mean?

In C, `void` is considered a datatype but you can consider it a keyword that means "no data"

```cpp
void setup() {...}
```

return no data

<!-- .slide: style="text-align: left;"> -->

---
## Let's simplify our code a little

Currently, at the start of our loop we have the following code: 

```cpp
void loop() {
  leftButton = digitalRead(btn_left);
  rightButton = digitalRead(btn_right);
  if (leftButton) {
    state = SCROLL_LEFT;
  } else if (rightButton){
    state = SCROLL_RIGHT;
  }
  // stuff happens down here
}
```

<!-- .slide: style="text-align: left;"> -->

---
## Let's clean it up a little

```cpp
int checkSensors(int btn_left, int btn_right){
  leftButton = digitalRead(btn_left);
  rightButton = digitalRight(btn_right);
  if (leftButton) {
    state = SCROLL_LEFT;
  } else if (rightButton){
    state = SCROLL_RIGHT;
  } else {
    state == STOP;
  }
}
void loop(){
    state = checkSensors(btn_left, btn_right);
    // stuff happens
}
```

<!-- .slide: style="text-align: left;"> -->

---
## Let's clean up some more

Elsewhere in our main loop we have this: 

```cpp
void loop(){
    state = checkSensors(btn_left, btn_right);
    // stuff
    else if (state == STOP){
        digitalWrite(13, LOW);
        digitalWrite(12, LOW);
        digitalWrite(11, LOW);
        digitalWrite(10, LOW);
        digitalWrite(9, LOW);
        digitalWrite(8, LOW);
        state = STOP;
    }
}
```

<!-- .slide: style="text-align: left;"> -->

---
## Let's clean that up

```cpp
int stopLEDs(int state){
    digitalWrite(13, LOW);
    digitalWrite(12, LOW);
    digitalWrite(11, LOW);
    digitalWrite(10, LOW);
    digitalWrite(9, LOW);
    digitalWrite(8, LOW);
  	return STOP;
}

void loop(){
    state = checkSensors(left_btn, right_btn);
    // stuff
    else if (state == STOP) {
        state = stopLEDs(state);
    }
}
```

<!-- .slide: style="text-align: left;"> -->

---
## Why are we passing and returning state

Trust me, that's for later ;)

<!-- .slide: style="text-align: left;"> -->

---
## Challenge! 

Go back and look at your scrolling lights program. Refactor your code so you use functions for each state and state gathering concept. Your loop function should look a bit like this

```cpp
void loop(){
    state = checkSensors(btn_left, btn_right);
    if (state == SCROLL_LEFT) {
        state = scrollLeft();
    } // continue your loop
}
```

<!-- .slide: style="text-align: left;"> -->
