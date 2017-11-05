"""
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        '''new_square is a class method and is called on the class,rather
        than on an instance of the class. It returns a new object of the
        class cls.'''
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())
"""

# """


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        print("__init__")

    def calculate_area(self):
        print("calculate_area")
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        '''new_square is a class method and is called on the class,rather
        than on an instance of the class. It returns a new object of the
        class cls.'''
        print("new_square")
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

rectangle = Rectangle(5, 6)
print(rectangle.calculate_area())
# 当创建一个类的实例时，默认情况下只有__init__被调用，如果类中定义了__del__方法，则该
# 方法也有可能被调用（可能与Python的垃圾回收机制有关）
# """
