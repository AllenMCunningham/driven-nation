#include <vl53l0x_platform.h>
#include <vl53l0x_def.h>
#include <vl53l0x_platform_log.h>
#include <vl53l0x_api_core.h>
#include <vl53l0x_i2c_platform.h>
#include <vl53l0x_tuning.h>
#include <vl53l0x_api.h>
#include <vl53l0x_device.h>
#include <vl53l0x_api_ranging.h>
#include <vl53l0x_api_strings.h>
#include <vl53l0x_interrupt_threshold_settings.h>
#include <Adafruit_VL53L0X.h>
#include <vl53l0x_api_calibration.h>
#include <vl53l0x_types.h>

/* This example shows how to use continuous mode to take
range measurements with the VL53L0X. It is based on
vl53l0x_ContinuousRanging_Example.c from the VL53L0X API.

The range readings are in units of mm. */


VL53L0X sensor;

void setup()
{
  Serial.begin(9600);
  Wire.begin();

  sensor.setTimeout(500);
  if (!sensor.init())
  {
    Serial.println("Failed to detect and initialize sensor!");
    while (1) {}
  }

  // Start continuous back-to-back mode (take readings as
  // fast as possible).  To use continuous timed mode
  // instead, provide a desired inter-measurement period in
  // ms (e.g. sensor.startContinuous(100)).
  sensor.startContinuous();
}

void loop()
{
  Serial.print(sensor.readRangeContinuousMillimeters());
  if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }

  Serial.println();
}

void loop()
{
  Serial.print(sensor.readRangeContinuousMillimeters());
  if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }

  Serial.println();
}
