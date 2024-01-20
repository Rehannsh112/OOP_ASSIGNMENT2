from abc import ABC

from CircuitComponent import CircuitComponent


class Buzzer(CircuitComponent):

    def __init__(self, priceDollar, priceCent, name, voltage, current, soundPressure, frequency):
        super().__init__(priceDollar, priceCent, name)
        self.voltage = voltage
        self.current = current
        self.soundPressure = soundPressure
        self.frequency = frequency

    def displayDetailsCSV(self):
        return f"{self.name}, {self.priceDollar}.{self.priceCent}, {self.voltage}, {self.current}, {self.soundPressure}, {self.frequency}"

    def displayDetails(self):
        return f"{self.name} - Voltage: {self.voltage}V, Current: {self.current}mA, Sound Pressure: {self.soundPressure}dB, Frequency: {self.frequency}Hz - ${self.priceDollar}.{self.priceCent}"

    def calculateWattage(self):
        return self.voltage * self.current / 1000  # Convert current from mA to A

    def convertValuesToCCV(self):
        return f"{self.voltage},{self.current},{self.soundPressure},{self.frequency},{self.name},{self.priceDollar},{self.priceCent}"

    def duplicate(self, obj):
        if isinstance(obj, Buzzer):
            return Buzzer(obj.priceDollar, obj.priceCent, obj.name, obj.voltage, obj.current, obj.soundPressure,
                          obj.frequency)
        return None

    def parsesToWireObject(self, value):
        values = value.split(',')
        return Buzzer(float(values[1]), int(values[2]), values[0], float(values[1]), float(values[2]),
                      float(values[3]), float(values[4]))

    def equals(self, obj):
        if isinstance(obj, Buzzer):
            return (
                    super().equals(obj) and
                    obj.voltage == self.voltage and
                    obj.current == self.current and
                    obj.soundPressure == self.soundPressure and
                    obj.frequency == self.frequency
            )
        return False
