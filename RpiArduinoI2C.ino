// https://github.com/bphermansson/RpiArduinoI2C

/*
 * Upload changes to Github:
 * git commit AS2.py
 * git push origin master
 * Update from Github
 * git pull * 
 * 
 */
 
// For I2C:
#include <Wire.h>
#define SLAVE_ADDRESS 0x04
int number = 0;
// Set D8 high when requesting to send a message tp the Rpi
int i2cInt = 8;

void setup() {
  // initialize I2c as slave
  Wire.begin(SLAVE_ADDRESS);
  // define callbacks for i2c communication
  //Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  // Send message to Rpi
  pinMode(i2cInt, OUTPUT);
  digitalWrite(i2cInt, HIGH);
  number = 3;
  sendData();
  delay(50);
  digitalWrite(i2cInt, LOW);
}

void loop() {

}

// Callback for sending data
void sendData(){
  Wire.write(number);
}
