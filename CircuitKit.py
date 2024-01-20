from typing import List
import PowerSource
from CircuitComponent import CircuitComponent


class CircuitKit:
    def __init__(self, name, components):
        self.name = name
        self.components = components
        self.price = self.calculateTotalPrice()
        self.componentCount = len(components)
        self.isFunctional = self.isFunctionalCheck()
        self.type = self.determineType()

    def addComponent(self, comp):
        if isinstance(comp, CircuitComponent):
            self.components.append(comp)
            self.updateAttributes()
            return True
        return False

    def removeComponent(self, comp):
        if comp in self.components:
            self.components.remove(comp)
            self.updateAttributes()
            return True
        return False

    def isValidPowerSource(self):
        powerSources = [comp for comp in self.components if isinstance(comp, PowerSource)]
        return len(powerSources) == 1

    def isFunctional(self):
        return self.isFunctional

    def isEqual(self, obj):
        if isinstance(obj, CircuitKit):
            return (
                    self.name == obj.name and
                    self.components == obj.components and
                    self.price == obj.price and
                    self.componentCount == obj.componentCount and
                    self.isFunctional == obj.isFunctional and
                    self.type == obj.type
            )
        return False

    def displayNumOfComponents(self):
        return len(self.components)

    def displayPowerSourceDetails(self):
        powerSources = [comp for comp in self.components if isinstance(comp, PowerSource)]
        if powerSources:
            return powerSources[0].displayDetails()
        return "No valid power source in the circuit kit."

    def displayType(self):
        return self.type

    def calculateTotalPrice(self):
        return sum(comp.priceDollar + comp.priceCent / 100 for comp in self.components)

    def isFunctionalCheck(self):
        return False

    def determineType(self):
        return "Unknown"

    def updateAttributes(self):
        self.price = self.calculateTotalPrice()
        self.componentCount = len(self.components)
        self.isFunctional = self.isFunctionalCheck()
        self.type = self.determineType()

