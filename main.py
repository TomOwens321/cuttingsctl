#!/usr/bin/env python
from lib.relay import Relay
import time

PIN = "P9_11"
FREQ = 0.5      # minutes
DURATION = 4.5   # seconds

relay = Relay(PIN)

while(1):
    relay.timed(DURATION)
    time.sleep(FREQ * 60)