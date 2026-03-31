class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def pace(self):
        print(f"The {self.color} car is driving at {self.speed} km/h")

car = Car("red", 120)
car.pace()