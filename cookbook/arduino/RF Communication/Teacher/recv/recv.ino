#include <RadioHead.h>
#include <RH_ASK.h>
#include <SPI.h>

#define RECV_PIN 6
#define MSG_PIN 5

#define debug(x) Serial.print(x); Serial.print(" ")
#define debugln(x) Serial.println(x);

RH_ASK driver;
uint8_t buf[12];
uint8_t buflen = sizeof(buf);

void setup() {
  Serial.begin(57600);
  Serial.println("INIT BOARD:");
  if (!driver.init()) {
    Serial.println("DRIVER INIT FAILED");
  }
  Serial.println("RX GO!");
  pinMode(RECV_PIN, OUTPUT);
  pinMode(MSG_PIN, OUTPUT);
  for (int i = 0; i < 10; i++) {
    digitalWrite(MSG_PIN, LOW);
    digitalWrite(RECV_PIN, HIGH);
    delay(100);
    digitalWrite(MSG_PIN, HIGH);
    digitalWrite(RECV_PIN, LOW);
    delay(100);
  }
}

void loop() {

  if (driver.available()) debugln("WHAT?");
  if (driver.recv(buf, &buflen)) {
    for (int i = 0; i < 10; i++) {
      digitalWrite(RECV_PIN, HIGH);
      delay(100);
      digitalWrite(RECV_PIN, LOW);
      delay(100);
    }
  }
  Serial.print("Message: ");
  Serial.println((char*)buf);

}
