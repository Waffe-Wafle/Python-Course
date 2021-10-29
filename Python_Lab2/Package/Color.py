class FigureColor:
    def __init__(self):
        self.COLOR = None

    @property
    def Color_Property(self):
        return self.COLOR

    @Color_Property.setter
    def Color_Property(self, Value):
        self.COLOR = Value