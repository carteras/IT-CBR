
#include <Servo.h> 
String readString; 
Servo myservo;  
int n; 

void setup() {
  Serial.begin(9600);
  myservo.writeMicroseconds(1500); 
  myservo.attach(8, 500, 2500);  
  Serial.println("servo all-in-one test code 12-25-13"); 
  Serial.println();
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();  
    readString += c; 
    delay(2);  
  }

  if (readString.length() >0) {
    Serial.println(readString);  

      
    if (readString == "d") { 
      while (digitalRead(7)) {} 
      myservo.detach(); 
      Serial.println("servo detached");
      goto bailout; 
    }
    if (readString == "a") {
      myservo.attach(7); 
      Serial.println("servo attached");
      goto bailout;
    }    

    n = readString.toInt();  

    
    if(n >= 500)
    {
      Serial.print("writing Microseconds: ");
      Serial.println(n);
      myservo.writeMicroseconds(n);
    }
    else
    {   
      Serial.print("writing Angle: ");
      Serial.println(n);
      myservo.write(n); 
    }

bailout: 
    Serial.print("Last servo command position: ");    
    Serial.println(myservo.read());
    Serial.println();
    readString=""; //empty for next input
  }
}
