from abc import ABC, abstractmethod


class CircuitComponent(ABC):
    def __init__(self, priceDollar, priceCent, name):
        self.priceDollar = priceDollar
        self.priceCent = priceCent
        self.name = name

    @abstractmethod
    def displayDetails(self):
        pass

    @abstractmethod
    def convertValuesToCCV(self):
        pass

    @abstractmethod
    def duplicate(self, obj):
        pass

    @abstractmethod
    def parsesToWireObject(self, value):
        pass

    @abstractmethod
    def equals(self, obj):
        pass
