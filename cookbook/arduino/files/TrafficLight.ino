// traffic light

int trafficGreenLED = 11;
int trafficOrangeLED = 12;
int trafficRedLED = 13;

// ped light

int pedGreenLED = 3;
int pedRedLED = 4;

// ped button

int pedButton = 2;
int pedButtonValue = 0;

int DELAY_LONG = 1000;
int DELAY_SHORT = 500;
int DELAY_VSHORT = 200;

void setup()
{
  pinMode(trafficGreenLED, OUTPUT);
  pinMode(trafficOrangeLED, OUTPUT);
  pinMode(trafficRedLED, OUTPUT);
  pinMode(pedGreenLED, OUTPUT);
  pinMode(pedRedLED, OUTPUT);
  
  pinMode(pedButton, INPUT);
  
  digitalWrite(trafficGreenLED, HIGH);
  digitalWrite(pedRedLED, HIGH);
  Serial.begin(115200);
}

void runLights() {
  delay(DELAY_LONG);
  digitalWrite(trafficGreenLED, LOW);
  digitalWrite(trafficOrangeLED, HIGH);

  delay(DELAY_SHORT);
  digitalWrite(trafficOrangeLED, LOW);
  digitalWrite(trafficRedLED, HIGH);

  delay(DELAY_SHORT);
  digitalWrite(pedRedLED, LOW);
  digitalWrite(pedGreenLED, HIGH);

  delay(DELAY_LONG);

  digitalWrite(pedRedLED, HIGH);
  digitalWrite(pedGreenLED, LOW);

  delay(DELAY_VSHORT);

  digitalWrite(pedRedLED, LOW);
  digitalWrite(pedGreenLED, HIGH);

  delay(DELAY_VSHORT);

  digitalWrite(pedRedLED, HIGH);
  digitalWrite(pedGreenLED, LOW);

  delay(DELAY_VSHORT);
  digitalWrite(pedRedLED, HIGH);

  delay(DELAY_SHORT);

  digitalWrite(trafficRedLED, LOW);
  digitalWrite(trafficGreenLED, HIGH);
}

void loop()
{
  pedButtonValue = digitalRead(pedButton);
  Serial.println(pedButtonValue);
  if (pedButtonValue == 1) {
    runLights();    
  }
  
  
}