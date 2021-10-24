from Package.Rectangle import Rectangle

class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, Color, Size):
        self.SIZE  = Size
        super().__init__(Color, self.SIZE, self.SIZE)

    @classmethod
    def Get_Figure_Type(Cls):
        return Cls.FIGURE_TYPE

    def __repr__(self):
        return "{} {} цвета радиусом {} площадью {}".format(
            Cire.get_figure_type(),
            self.FigureColor.Color_Property,
            self.SIZE,
            self.square()
        )