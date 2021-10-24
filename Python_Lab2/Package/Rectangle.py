from Package.Figure import Figure
from Package.Color  import FigureColor

class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, Color, Width, Height):
        self.WIDTH = Width
        self. HEIGHT = Height
        self.FC = FigureColor()
        self.FC.Color_Property = Color

    @classmethod
    def Get_Figure_Type(Cls):
        return Cls.FIGURE_TYPE

    def __repr__(self):
        return "{}{} цвета шириной {} и высотой {} площадью {}".format(
            Rectangle.Get_Figure_Type(),
            self.FC.Color_Property,
            self.WIDTH,
            self.HEIGHT,
            self.square()
        )