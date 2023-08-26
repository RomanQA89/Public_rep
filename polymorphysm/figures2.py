from figures import Rectangle, Square, Circle

rect1 = Rectangle(5,7)
rect2 = Rectangle(3,9)

print(rect1.getArea(), rect2.getArea())

square1 = Square(4)
square2 = Square(6)

print(square1.getAreaSquare(), square2.getAreaSquare())

circle1 = Circle(2)
circle2 = Circle(7)

print(circle1.gerCircle(), circle2.gerCircle())

figures = [rect1, rect2, square1, square2, circle1, circle2]
for figure in figures:
    if isinstance(figure, Square):
        print('Площади квадратов:', figure.getAreaSquare())
    elif isinstance(figure, Circle):
        print('Площади окружностей:', figure.gerCircle())
    else:
        print('Площади прямоугольников:', figure.getArea())
