# Answer


Arduino 2
```cpp
#define debug(x) Serial.print(x); Serial.print(" ")
#define debugln(x) Serial.println(x);

#define green_btn 12
#define yellow_btn 11
#define red_btn 10

int pressed_green = 0;
int pressed_yellow = 0; 
int pressed_red = 0;

int msgSent = 0;

int OFF = 0;
int GREEN = 1;
int YELLOW = 2;
int RED = 3;
int STATE = OFF ;
  
  
int turnedOff(){
  return RED;
}

int redLightOn(int grn, int ylw, int red){
  if (grn == 1) return GREEN;
  if (ylw == 1) return YELLOW;
  if (red == 1) {
    Serial.write("r\n");
    digitalWrite(13, HIGH);
  }
  //debugln("red led go now");
  //Serial.write("r\n");
  return RED;
}

int yellowLightOn(int grn, int ylw, int red){
  if (grn == 1) return GREEN;
  if (ylw == 1) {
    Serial.write("y\n");
    digitalWrite(13, HIGH);
  }
  if (red == 1) return RED;
  return YELLOW;
}

int greenLightOn(int grn, int ylw, int red){
  if (grn == 1) {
    digitalWrite(13, HIGH);
    Serial.write("g\n");
  }
  if (ylw == 1) return YELLOW;
  if (red == 1) return RED;
  return GREEN;
}

void setup()
{
  for (int i = red_btn; i<=green_btn; i++){
    pinMode(i, INPUT);
  }
  pinMode(13, OUTPUT);
  Serial.begin(115200);
}

void loop()
{
  pressed_red = digitalRead(red_btn);
  pressed_yellow = digitalRead(yellow_btn);
  pressed_green = digitalRead(green_btn);
  
  if (STATE == OFF){
    STATE = turnedOff();
  } else if (STATE == RED){
    STATE = redLightOn(pressed_green, pressed_yellow, pressed_red);
  } else if (STATE == YELLOW){
    STATE = yellowLightOn(pressed_green, pressed_yellow, pressed_red);
  } else if (STATE == GREEN){
    STATE = greenLightOn(pressed_green, pressed_yellow, pressed_red);
  }
}
```


Arduino 1

```cpp
#define green 2
#define yellow 3
#define red 4

void enableLight(char led){
  int foo; 
  if (led == 'g') foo = green;
  if (led == 'y') foo = yellow;
  if (led == 'r') foo = red;
  
  digitalWrite(foo, HIGH);
  for (int i = green; i <=red; i++){
    if (foo != i) digitalWrite(i, LOW);
  }
}


void serialEvent(){
  int incommingByte = Serial.read();
  Serial.print("I have recieved ");
  Serial.println((char) incommingByte);
  enableLight((char) incommingByte);
}


void setup()
{
  for (int i = green; i <=red; i++){
    pinMode(i, OUTPUT);
  }
  Serial.begin(115200);
}

void loop()
{
}


```
