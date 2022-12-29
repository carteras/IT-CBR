// C++ code
//
#include <Wire.h>

#define MIN_VAL 7
#define MAX_VAL 12
#define POT_PIN A0

int potVal = 0;
void setup()
{
  pinMode(POT_PIN, INPUT);
  Wire.begin(8);
  Wire.onRequest(requestEvent);
}

void loop()
{
  delay(100);
  
}

void requestEvent(){
  potVal = analogRead(POT_PIN);
  potVal = map(potVal, 0, 1023, MIN_VAL, MAX_VAL);
  Wire.write(potVal);
}