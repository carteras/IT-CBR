#include <RadioHead.h>
#include <RH_ASK.h>
#include <SPI.h>


#define SEND_PIN 7

#define debug(x) Serial.print(x); Serial.print(" ")
#define debugln(x) Serial.println(x);

//RH_ASK driver(2000, 11, 12, 0);
RH_ASK driver;
const char *msg = "foo";



void setup() {
  Serial.begin(57600);
  if (!driver.init()) {
    Serial.println("DRIVER INIT FAILED");
  }
  Serial.println("RX GO!");
  pinMode(SEND_PIN, OUTPUT);

  for (int i = 0; i < 10; i++) {
    digitalWrite(SEND_PIN, LOW);
    delay(100);
    digitalWrite(SEND_PIN, HIGH);
    delay(100);
  }


}

void sendMessage() {
  driver.send((uint8_t *)msg, strlen(msg));
  driver.waitPacketSent();
}




void loop() {

  digitalWrite(SEND_PIN, HIGH);
  sendMessage();
  digitalWrite(SEND_PIN, LOW);
  delay(100);

}
