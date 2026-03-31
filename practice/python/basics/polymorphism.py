class Dog:
    def speak(self):
        print("Dog Barks")


class Cat:
    def speak(self):
        print("Cat Meows")


for animal in [Dog(), Cat()]:
    animal.speak()