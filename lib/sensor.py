import Adafruit_BBIO.ADC as ADC

class Sensor:
    def __init__(self, pin):
        self.pin = pin
        self.name = pin
        ADC.setup()
        
    def get_value(self):
        return ADC.read(self.pin)