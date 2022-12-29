// C++ code
//
#define MIN_PIN 7
#define MAX_PIN 12

int incomingByte = MIN_PIN;

void setup()
{
  for (int i = MIN_PIN; i <= MAX_PIN; i++){
    pinMode(i, OUTPUT);
  }
  Serial.begin(9600);
}

void loop()
{
  while (Serial.available() > 0){
    incomingByte = (int) Serial.read();
    Serial.println(incomingByte);
    for (int i = MIN_PIN; i <= MAX_PIN; i++){
      if (incomingByte == i){
        digitalWrite(i, HIGH);
      } else {
        digitalWrite(i, LOW);
      }
    }
  }
}