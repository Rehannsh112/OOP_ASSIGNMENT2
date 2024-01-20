from enum import Enum, auto
from CircuitComponent import CircuitComponent


class SensorType(Enum):
    MOVEMENT = auto()
    INFRARED = auto()
    LIGHT = auto()
    TEMPERATURE = auto()
    HUMIDITY = auto()
    SOUND = auto()
    DUST = auto()


class Sensor(CircuitComponent):
    def __init__(self, priceDollar, priceCent, name, voltage, isActive, sensorType):
        super().__init__(priceDollar, priceCent, name)
        self.voltage = voltage
        self.isActive = isActive
        self.sensorType = sensorType

    def displayDetailsCSV(self):
        return f"{self.name}, {self.priceDollar}.{self.priceCent}, {self.voltage}, {int(self.isActive)}, {self.sensorType.name}"

    def duplicate(self, obj):
        if isinstance(obj, Sensor):
            return Sensor(obj.priceDollar, obj.priceCent, obj.name, obj.voltage, obj.isActive, obj.sensorType)
        return None

    def parsesToWireObject(self, value):
        values = value.split(',')
        return Sensor(float(values[1]), int(values[2]), values[0], float(values[3]), bool(int(values[4])),
                      SensorType[values[5]])

    def convertValuesToCCV(self):
        return f"{self.voltage},{self.name},{self.priceDollar},{self.priceCent},{str(self.isActive)},{self.sensorType}"

    def equals(self, obj):
        if isinstance(obj, Sensor):
            return (
                    super().equals(obj) and
                    obj.voltage == self.voltage and
                    obj.isActive == self.isActive and
                    obj.sensorType == self.sensorType
            )
        return False

    def displayDetails(self):
        return f"{self.name} - Voltage: {self.voltage}V, Active: {self.isActive}, Type: {self.sensorType.name} - ${self.priceDollar}.{self.priceCent}"
