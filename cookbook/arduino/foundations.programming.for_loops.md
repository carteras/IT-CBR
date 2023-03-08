# How does something work?

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* What?

## Concepts

In Arduino, a for loop is a programming structure that allows you to repeat a set of instructions a specified number of times. It is often used when you need to perform a task multiple times, such as iterating over an array or a sequence of values.

Here is the basic syntax for a for loop in Arduino:

```cpp
for (initialization; condition; increment) {
   // statement(s) to be executed repeatedly
}
```
The initialization section is where you set the starting value for the loop counter variable. This is typically used to initialize a variable that will be used in the loop.

The condition section is where you specify the condition that must be true for the loop to continue. The loop will continue to execute as long as this condition is true.

The increment section is where you specify how the loop counter variable should be incremented after each iteration of the loop.

The statements inside the curly braces {} will be executed repeatedly for each iteration of the loop.

For example, the following code will print the numbers 0 to 9 to the serial monitor:


```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  for (int i = 0; i < 10; i++) {
    Serial.println(i);
  }
  delay(1000);
}
```

In this code, the loop counter variable i is initialized to 0, and the loop will continue to execute as long as i is less than 10. After each iteration of the loop, i is incremented by 1. The Serial.println(i) statement inside the loop will print the current value of i to the serial monitor. The delay(1000) statement outside the loop will pause the program for 1 second before starting the loop again.

Overall, for loops are a powerful and versatile tool in Arduino programming that can help simplify complex tasks and make your code more efficient.

## Practice Question

Create a program that makes an LED "chase" back and forth between four pins. The LED should light up for a short period of time, then move to the next pin and repeat. The pattern should repeat continuously.

Here are the requirements for this program:

Use four digital output pins to control the LEDs (for example, pins 2, 3, 4, and 5).
Use a for loop to iterate through each LED pin in sequence.
Use another for loop to blink the LED on each pin for a short period of time (for example, 100 milliseconds).
Use the digitalWrite() function to turn the LEDs on and off.