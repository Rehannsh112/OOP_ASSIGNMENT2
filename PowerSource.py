from abc import abstractmethod
from CircuitComponent import CircuitComponent


class PowerSource(CircuitComponent):
    def __init__(self, priceDollar, priceCent, name, voltage):
        super().__init__(priceDollar, priceCent, name)
        self.voltage = voltage

    @abstractmethod
    def displayDetailsCSV(self):
        return f"{self.name}, {self.priceDollar}.{self.priceCent}, {self.voltage}"

    def displayDetails(self):
        return f"{self.voltage}mm {self.name} ${self.priceDollar}.{self.priceCent}"

    def convertValuesToCCV(self):
        return f"{self.voltage},{self.name},{self.priceDollar},{self.priceCent}"

    def duplicate(self, obj):
        pass

    def parsesToWireObject(self, value):
        pass

    def equals(self, obj):
        if isinstance(obj, PowerSource):
            return (
                obj.priceDollar == self.priceDollar and
                obj.priceCent == self.priceCent and
                obj.name == self.name and
                obj.voltage == self.voltage
            )
        return False
