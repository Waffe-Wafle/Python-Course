from Package.Figure import Figure
from Package.Color  import FigureColor
import math

class Circle(Figure):
    FIGURE_TYPE = "Круг"
    def __init__(self, Color, Size):
        self.SIZE  = Size
        self.FC = FigureColor()
        self.FC.Color_Property = Color

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
        
