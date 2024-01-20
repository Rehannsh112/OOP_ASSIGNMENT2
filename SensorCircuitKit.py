from CircuitKit import CircuitKit
from Sensor import Sensor
from PowerSource import PowerSource
from Buzzer import Buzzer
from LED import LED
from Switch import Switch
from Batterie import Batterie


class SensorCircuitKit(CircuitKit):
    def __init__(self, name, sensor, powerSource, buzzer, lights, switches):
        super().__init__(name, [sensor, powerSource, buzzer] + lights + switches)
        self.sensor = sensor
        self.powerSource = powerSource
        self.buzzer = buzzer
        self.lights = lights
        self.switches = switches

    def isAllLightsSame(self):
        # check if all lights are of the same type and have matching attributes
        return all(isinstance(light, LED) for light in self.lights)

    def displayPowerSupplyDetails(self):
        return f"Power Supply: {self.powerSource.displayDetails()}"

    def displayTypeOfSensorUsing(self):
        return f"Sensor Type: {self.sensor.type}"

    def displayLightDetails(self):
        lightDetails = "\n".join(light.displayDetails() for light in self.lights)
        return f"Light Details:\n{lightDetails}"
