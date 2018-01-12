#!/usr/bin/env python
from lib.relay import Relay
from lib.sensor import Sensor
import time

PIN = "P9_11"
FREQ = 0.5      # minutes
DURATION = 4.5   # seconds
SENSOR = "AIN1"

relay = Relay(PIN)
sensor = Sensor(SENSOR)

while(1):
    relay.timed(DURATION)
    print "Sensor value: %f" % sensor.get_value()
    time.sleep(FREQ * 60)