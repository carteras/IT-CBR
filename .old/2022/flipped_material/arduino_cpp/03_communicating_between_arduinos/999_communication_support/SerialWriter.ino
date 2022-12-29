// C++ code
//
#define MIN_VAL 7
#define MAX_VAL 12
#define POT_PIN A0

int potVal = 0;
void setup()
{
  pinMode(POT_PIN, INPUT);
  Serial.begin(9600);
}

void loop()
{
  potVal = analogRead(POT_PIN);
  potVal = map(potVal, 0, 1023, MIN_VAL, MAX_VAL);
  Serial.write(potVal);
}