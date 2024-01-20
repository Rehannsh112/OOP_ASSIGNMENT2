from abc import abstractmethod
from CircuitComponent import CircuitComponent


class Light(CircuitComponent):
    def __init__(self, priceDollar, priceCent, name, voltage, current):
        super().__init__(priceDollar, priceCent, name)
        self.voltage = voltage
        self.current = current

    @abstractmethod
    def displayDetailsCSV(self):
        pass

    @abstractmethod
    def calculateWattage(self):
        pass

    def displayDetails(self):
        return f"{self.voltage}V {self.current}mA {self.name} ${self.priceDollar}.{self.priceCent}"

    def convertValuesToCCV(self):
        return f"{self.voltage},{self.current},{self.name},{self.priceDollar},{self.priceCent}"

    def duplicate(self, obj):
        pass

    def parsesToWireObject(self, value):
        pass

    def equals(self, obj):
        pass
