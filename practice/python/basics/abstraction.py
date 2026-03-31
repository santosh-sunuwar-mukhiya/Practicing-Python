from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

c = Circle()
print(c.area())