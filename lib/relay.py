import Adafruit_BBIO.GPIO as GPIO
from threading import Thread
import time

class Relay:
    def __init__(self, pin):
        self.pin = pin
        self.name = pin
        self.state = 0
        self._setup(self.pin)
        
    def turn_on(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.state = 1
        
    def turn_off(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.state = 0
        
    def _pulse(self, timer):
        self.turn_on()
        time.sleep(timer)
        self.turn_off()
        
    def timed(self, timer):
        t = Thread(target=self._pulse, args=(timer,))
        t.start()
        
    def _setup(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        