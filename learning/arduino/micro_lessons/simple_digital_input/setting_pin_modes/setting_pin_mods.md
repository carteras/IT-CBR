# Setting Pin Modes

## Topics covered

"At the end of this learning brief, you will be able to answer the following questions"

* What is a pin
* What are pin modes
* How to set a pin mode

## Learning Resources

* [Digital Pins](https://docs.arduino.cc/learn/microcontrollers/digital-pins)
* [Pin Modes](https://docs.arduino.cc/learn/microcontrollers/digital-pins)

## Topics

### What are pins?

Broadly speaking, pins are how the micro-controller can talk to sensors and actuators.

### What is a Pin Mode

Pins can be set as `INPUT` or `OUTPUT` pins.

`INPUT` pins are restricted to reading information from elsewhere like a button or a sensor.

`OUTPUT` pins write to actuators like an LED

```cpp
void setup() {
  pinMode(13, OUTPUT);    // sets the digital pin 13 as output
}

void loop() {
  digitalWrite(13, HIGH); // sets the digital pin 13 on
  delay(1000);            // waits for a second
  digitalWrite(13, LOW);  // sets the digital pin 13 off
  delay(1000);            // waits for a second
}
```
