#include <Wire.h> 

#define MIN_PIN 7
#define MAX_PIN 12

int incomingByte = MIN_PIN;

void setup()
{
  for (int i = MIN_PIN; i <= MAX_PIN; i++){
    pinMode(i, OUTPUT);
  }
  Wire.begin();
}

void loop()
{
  Wire.requestFrom(8, 1); 
  while (Wire.available() > 0){
    incomingByte = (int) Wire.read();
    Serial.println(incomingByte);
    for (int i = MIN_PIN; i <= MAX_PIN; i++){
      if (incomingByte == i){
        digitalWrite(i, HIGH);
      } else {
        digitalWrite(i, LOW);
      }
    }
  }
  delay(100);
}