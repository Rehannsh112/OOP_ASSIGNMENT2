from PowerSource import PowerSource


class Batterie(PowerSource):
    def __init__(self, priceDollar, priceCent, name, voltage, size):
        super().__init__(priceDollar, priceCent, name, voltage)
        self.size = size

    def displayDetailsCSV(self):
        return f"{self.name}, {self.priceDollar}.{self.priceCent}, {self.voltage}, {self.size}"

    def duplicate(self, obj):
        if isinstance(obj, Batterie):
            return Batterie(obj.priceDollar, obj.priceCent, obj.name, obj.voltage, obj.size)
        return None

    def parsesToWireObject(self, value):
        values = value.split(',')
        return Batterie(float(values[3]), 0, values[1], float(values[2]), values[0])

    def equals(self, obj):
        if isinstance(obj, Batterie):
            return (
                    super().equals(obj) and
                    obj.size == self.size
            )
        return False
