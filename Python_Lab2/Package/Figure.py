from abc import ABC, abstractmethod
from math import pi
class Figure(ABC):
    @abstractmethod
    def square(self):
        if self.FIGURE_TYPE == "Круг":
            return pi*(self.Sise*self.Sise)
        elif self.FIGURE_TYPE == "Прямоугольник":
            return self.Size*self.Sise

        from abc import ABC, abstractmethod