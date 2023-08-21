# Making Actions Based on Conditions

## Problem

You want to execute a block of code only if a particular condition is true. For example,
you may want to light an LED if a switch is pressed or if an analog value is greater than
some threshold.

## Solution

The following code uses the wiring shown in Recipe 5.1:

```c++
    /*
    Pushbutton sketch
    a switch connected to pin 2 lights the LED on pin 13
    */
    const int ledPin = 13; // choose the pin for the LED
    const int inputPin = 2; // choose the input pin (for a pushbutton)
    void setup() {
        pinMode(ledPin, OUTPUT); // declare LED pin as output
        pinMode(inputPin, INPUT); // declare pushbutton pin as input
    }
    void loop(){
        int val = digitalRead(inputPin); // read input value
        if (val == HIGH) // check if the input is HIGH
        {
            digitalWrite(ledPin, HIGH); // turn LED on if switch is pressed
        }
    }
```


## Discussion

The if statement is used to test the value of digitalRead. An if statement must have a
test within the parentheses that can only be true or false. In the example in this recipe’s

Solution, it’s val == HIGH, and the code block following the if statement is only exe-
cuted if the expression is true. A code block consists of all code within the brackets (or
if you don’t use brackets, the block is just the next executable statement terminated by
a semicolon).
If you want to do one thing if a statement is true and another if it is false, use the
if...else statement:

```cpp
    /*
    Pushbutton sketch
    a switch connected to pin 2 lights the LED on pin 13
    */
    const int ledPin = 13; // choose the pin for the LED
    const int inputPin = 2; // choose the input pin (for a pushbutton)
    void setup() {
        pinMode(ledPin, OUTPUT); // declare LED pin as output
        pinMode(inputPin, INPUT); // declare pushbutton pin as input
    }
    void loop(){
    int val = digitalRead(inputPin); // read input value
        if (val == HIGH) // check if the input is HIGH
        {
        // do this if val is HIGH
            digitalWrite(ledPin, HIGH); // turn LED on if switch is pressed
        }
        else
        {
        // else do this if val is not HIGH
            digitalWrite(ledPin, LOW); // turn LED off
        }
    }
```