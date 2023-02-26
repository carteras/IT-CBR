# What are digital signals? 

## Learning Goals

*By the end of this recipe you should be able to answer the following:*

* What do we mean by signals? 
* What are digital signals?


## Concepts

Electronic SIgnals: electrical engineering loosely defines a signal as how voltage changes over time.

Digital Signals have a finite set of possible values: 

* 0 and 1
* 0 or 5

[0 and 1](img/digital_signals.png)

### Example

```cpp

void setup(){
    // prepare to write digital output
    pinMode(13, OUTPUT); 
}

void loop(){
    //write 5v to pin 13
    digitalWrite(13, HIGH);
    delay(100);
    digitalWrite(13, LOW);
    delay(100); 
}

```

```cpp

void setup(){
    // setting pin 2 to be input
    pinMode(2, INPUT);

    Serial.begin(9600);
}

void loop(){
    // check to see what the value is
    int btnValue = digitalRead(2);

    // this will print 0 if low
    // or 1 if high
    Serial.println(btnValue);
}
```

Putting it together. 

Do this in tinkercad

Note: put a jump lead between pin 13 and straight into pin 2


```cpp
int btnValue;
void setup(){
    pinMode(13, OUTPUT);
    pinMode(2, INPUT);
    Serial.begin(9600);
}

void loop(){
    digitalWrite(13, HIGH);
    delay(100);
    btnValue = digitalRead(2);
    Serial.println(btnValue);
    digitalWrite(13, LOW);
    delay(100);
    btnValue = digitalRead(2);
    Serial.println(btnValue);
    delay(100);
}
```

Experiment with putting a resister between pin 13 and pin 2: 

Test with the following resisters: 

* 1ohm
* 220 ohms
* 512 ohms
* 1 Kohms
* 10 kohms

What is happening?


