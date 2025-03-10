class Shape:
    def __init__(self):
        # Initialization logic for the Shape class
        print("Shape initialized")

    def calculate_area(self):
        # Base class method that does nothing
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        # Call the Shape class's constructor using super()
        super().__init__()
        self.width = width
        self.height = height

    def calculate_area(self):
        # Implement the calculate_area method for Rectangle
        area = self.width * self.height
        print(f"Area of the rectangle: {area}")
        # Optionally, call the base class's calculate_area method if needed
        super().calculate_area()

# Demonstration
rectangle = Rectangle(6, 10)
rectangle.calculate_area()
