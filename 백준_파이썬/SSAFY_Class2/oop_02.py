# main.py


# 아래 클래스를 수정하시오.
class Shape:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'
    
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter
    
    def print_info(self):
        print(f'Width: {shape1.width}')
        print(f'Height: {shape1.height}')
        print(f'Area: {shape1.calculate_area()}')
        print(f'Perimeter: {shape1.calculate_perimeter()}')

shape1 = Shape(5, 3)
shape1.print_info()
print(shape1)