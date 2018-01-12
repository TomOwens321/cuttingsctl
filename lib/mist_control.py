from lib.sensor import Sensor
from lib.relay  import Relay
from lib.logger import Logger

class MistControl:
    
    def __init__(self, relayPin=None, sensorPin=None):
        
        if relayPin:
            Logger.logit("Setting up a relay")
            self.relay = Relay(relayPin)
        if sensorPin:
            Logger.logit("Setting up a sensor")
            self.sensor = Sensor(sensorPin)