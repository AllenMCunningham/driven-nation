#include "Adafruit_VL53L0X.h"

Adafruit_VL53L0X lox = Adafruit_VL53L0X();

void setup() {
  Serial.begin(9600);

  // wait until serial port opens for native USB devices
  while (! Serial) {
    delay(1);
  }

  Serial.println("Adafruit VL53L0X test.");
  if (!lox.begin()) {
    Serial.println(F("Failed to boot VL53L0X"));
    while(1);
  }
  // power
  Serial.println(F("VL53L0X API Continuous Ranging example\n\n"));

  // start continuous ranging
  lox.startRangeContinuous();
}

void loop() {
  // average 5 readings
  uint8_t reading_count = 5;
  uint16_t sum = 0;
  for (uint8_t i = 0; i < reading_count; i++) {
    sum += lox.readRange();
  }
  Serial.print(sum / reading_count);
  Serial.println(" mm");
  
}
