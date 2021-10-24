from Package.Rectangle import Rectangle
from Package.Circle import Circle
from Package.Square import Square

def Main():
    Rectangle1 = Rectangle("белый", 10, 20)
    Circle1    = Circle   ("синий", 10)
    Square1    = Square   ("красный", 10)
    print(Rectangle1)
    print(Circle1)
    print(Circle1)

if __name__ == "__main__":
    Main()