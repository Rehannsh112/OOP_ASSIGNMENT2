from enum import Enum, auto
from CircuitComponent import CircuitComponent


class SwitchType(Enum):
    PUSH = auto()
    SLIDE = auto()
    ROCKER = auto()
    TOGGLE = auto()


class Switch(CircuitComponent):
    def __init__(self, priceDollar, priceCent, name, voltage, current, isActive, switchType):
        super().__init__(priceDollar, priceCent, name)
        self.voltage = voltage
        self.current = current
        self.isActive = isActive
        self.switchType = switchType

    def displayDetailsCSV(self):
        return (f"{self.name}, {self.priceDollar}.{self.priceCent}, {self.voltage}, {self.current},"
                f" {int(self.isActive)}"
                f", {self.switchType.name}")

    def displayDetails(self):
        return (f"{self.name} - Voltage: {self.voltage}V, Current: {self.current}mA, Active: {self.isActive},"
                f" Type: {self.switchType.name} - ${self.priceDollar}.{self.priceCent}")

    def calculateWattage(self):
        return self.voltage * self.current / 1000  # Convert current from mA to A

    def duplicate(self, obj):
        if isinstance(obj, Switch):
            return Switch(obj.priceDollar, obj.priceCent, obj.name, obj.voltage, obj.current, obj.isActive,
                          obj.switchType)
        return None

    def parsesToWireObject(self, value):
        values = value.split(',')
        return Switch(float(values[1]), int(values[2]), values[0], float(values[1]), float(values[2]),
                      bool(values[4]), values[3])

    def equals(self, obj):
        if isinstance(obj, Switch):
            return (
                    super().equals(obj) and
                    obj.voltage == self.voltage and
                    obj.current == self.current and
                    obj.isActive == self.isActive and
                    obj.switchType == self.switchType
            )
        return False

    def convertValuesToCCV(self):
        return (f"{self.voltage},{self.current},{int(self.isActive)},{self.switchType.name},"
                f"{self.name},{self.priceDollar},{self.priceCent}")
