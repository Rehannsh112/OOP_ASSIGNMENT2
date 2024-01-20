from CircuitComponent import CircuitComponent


class Wire(CircuitComponent):
    def __init__(self, priceDollar, priceCent, name, length):
        super().__init__(priceDollar, priceCent, name)
        self.length = length

    def displayDetailsCSV(self):
        return f"{self.name}, {self.priceDollar}.{self.priceCent}, {self.length}"

    def displayDetails(self):
        return f"{self.length}mm {self.name} ${self.priceDollar}.{self.priceCent}"

    def convertValuesToCCV(self):
        return f"{self.length},{self.name},{self.priceDollar},{self.priceCent}"

    def duplicate(self, obj):
        if isinstance(obj, Wire):
            return Wire(self.priceDollar, self.priceCent, self.name, obj.length)
        return None

    def parsesToWireObject(self, value):
        values = value.split(',')
        return Wire(float(values[2]), int(values[3]), values[1], int(values[0]))

    def equals(self, obj):
        if isinstance(obj, Wire):
            return self.length == obj.length
        return False
