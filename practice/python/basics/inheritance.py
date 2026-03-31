class Animal:
    def speak(self):
        print("Animal makes sound")


class Dog(Animal):
    def barks(self):
        print("Dog barks")


d = Dog()
d.speak()
d.barks()