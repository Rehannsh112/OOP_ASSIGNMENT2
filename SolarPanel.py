from PowerSource import PowerSource


class SolarPanel(PowerSource):
    def __init__(self, priceDollar, priceCent, name, voltage, current):
        super().__init__(priceDollar, priceCent, name, voltage)
        self.current = current

    def displayDetailsCSV(self):
        return f"{self.name}, {self.priceDollar}.{self.priceCent}, {self.voltage}, {self.current}"

    def calculateWattage(self):
        return self.voltage * self.current / 1000.0

    def duplicate(self, obj):
        if isinstance(obj, SolarPanel):
            return SolarPanel(obj.priceDollar, obj.priceCent, obj.name, obj.voltage, obj.current)
        return None

    def parsesToWireObject(self, value):
        values = value.split(',')
        return SolarPanel(float(values[3]), 0, values[2], float(values[0]), float(values[1]))

    def equals(self, obj):
        if isinstance(obj, SolarPanel):
            return (
                    super().equals(obj) and
                    obj.current == self.current
            )
        return False
