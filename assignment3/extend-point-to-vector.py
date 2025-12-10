# Within the assignment3 folder, create a file called extend-point-to-vector.py. !
# Create a class called Point. It represents a point in 2d space, with x and y values passed to the __init__() method. !
# It should include methods for equality, string representation, and Euclidian distance to another point.

# Create a class called Vector which is a subclass of Point and uses the same __init__() method. Add a method  !
# in the vector class which overrides the string representation so Vectors print differently than Points. 
# Override the + operator so that it implements vector addition, summing the x and y values and returning a new Vector.
# Print results which demonstrate all of the classes and methods which have been implemented.

# Create a class called Point. It represents a point in 2d space, with x and y values passed to the __init__() method.
#  It should include methods for equality, string representation, and Euclidian distance to another point.
# Create a class called Vector which is a subclass of Point and uses the same __init__() method. Add a method in the vector class which overrides the string representation so Vectors print differently than Points. Override the + operator so that it implements vector addition, summing the x and y values and returning a new Vector.
# Print results which demonstrate all of the classes and methods which have been implemented.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return  self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Point: {self.x}, {self.y}"
    
    def euclidian_dist(self):
        pass




class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)


    def __str__(self):
        return f"Vector: {self.x}, {self.y}"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

point1 = Point(1,2)
print(point1)
point2 = Point(3,4)
print(point2)
print(point1 == point2)

vector1 = Vector(4,5)
vector2 = Vector(6,7)
vector3 = Vector(4,5)
vector4 = vector2 + vector1
print(vector1)
print(vector2)
print(vector2 == vector3)
print(vector1 == vector3)
print(vector4)