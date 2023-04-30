# Vehicle Ride Height

## Problem:
In motorsports it is common to put linear potentiomiters on suspension components to measure their compression/rebound. This is by far the most accurate method to measure such things and downforce. However, I would like to develop a system that can attach to any vehicle temorarily and without modification to measure ride height. This data could then be extrapolated to generate a quantitative measure of downforce in real life situations.

## Proposed solution:
Measuering the distance from a sensor to the ground, and transmitting this data to a central compute source. We can use relative x and y position of sensors to each other, as well well as the ride height z to define the plane of the vehicle. 


## Sensor hardware
I am going to use arduino components for the individual sensors. they are cheap, and pleniful with robust documentation and comunity support. 

### Measuring Ride Height
Comparing distance sensors, Laser Time of Flight produced more accurate results than sonar sensors in the approximate range I would expect these sensors to mount. The 245/45/17 on my test vehicle have a diameter of ~650mm putting the axle center line at ~325mm which would be the ideal location to mount the sensor.

The resolution needed should not be greater than 2hz. in order to reduce noise, we shoud take an average on sensor readings across this time frame. 

### Communication
I have moved forward with using canbus to transmit data. this requires physical wires to connect each sensor, but reduces complexity of pairing multiple wireless devices. I think this will be a great v1 approach.

### Housing and Mounting
A 3d printed housing to fit the final components with an action cam stye mounting tab will be created. Using off the shelf suction cup mounts should be stable enough. 

## Processing
As of now I plan on reading and processing the canbus data using a rasbery pi and python. the first iteration may be to simply process and store the results for later analysis, but creating a real time dashboard would be very benifitial for continuous testing of aero components. 