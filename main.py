#!/usr/bin/env python
from lib.mist_control import MistControl
import time

PIN = "P9_11"
FREQ = 1.1      # minutes
DURATION = 4.5   # seconds
SENSOR = "AIN1"

mctl = MistControl(PIN, SENSOR)

while(1):
    mctl.relay.timed(DURATION)
    print "Sensor value: %f" % mctl.sensor.get_value()
    time.sleep(FREQ * 60)