#create inheritance using animal Dog relation.
# for example,
#     Animal and Dog both has same habitat so create a method for habitat
# use super() constructor for calling parent constructor.
# class Animal:
#     #code
#
# class Dog(Animal):
#     super()-it refers Animal class,now you can call Animal's methods.

class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def animal_sound(self) -> None:
        print("Animal makes sound")

class Dog(Animal):
    def __init__(self):
        super().__init__("Kennel")

    def sound(self):
        super().animal_sound()
        print("woof woof!")


x = Dog()
x.sound()
