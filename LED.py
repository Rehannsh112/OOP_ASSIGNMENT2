from Light import Light


class LED(Light):
    def __init__(self, priceDollar, priceCent, name, voltage, current, color):
        super().__init__(priceDollar, priceCent, name, voltage, current)
        self.color = color

    def displayDetailsCSV(self):
        return f"{self.name}, {self.priceDollar}.{self.priceCent}, {self.voltage}, {self.current}, {self.color}"

    def calculateWattage(self):
        return self.voltage * self.current / 1000  # convert current from mA to A

    def duplicate(self, obj):
        if isinstance(obj, LED):
            return LED(obj.priceDollar, obj.priceCent, obj.name, obj.voltage, obj.current, obj.color)
        return None

    def parsesToWireObject(self, value):
        values = value.split(',')
        return LED(float(values[1]), int(values[2]), values[0], float(values[1]), float(values[2]), values[3])

    def equals(self, obj):
        if isinstance(obj, LED):
            return (
                    super().equals(obj) and
                    obj.color == self.color
            )
        return False

