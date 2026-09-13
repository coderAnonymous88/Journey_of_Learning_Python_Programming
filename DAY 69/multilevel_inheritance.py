class Animal:
    def __init__(self , name , species):
        self.name = name
        self.species = species

    def show(self):
        print(f"Name of the Animal is {self.name}")
        print(f"Species of the Animal is {self.species}")

class Dog(Animal):
    def __init__(self , name , owner):
        Animal.__init__(self , name , species="Dog")
        self.owner = owner

    def show(self):
        Animal.show(self)
        print(f"The owner of the animal is {self.owner}")


class GoldenRetriver(Dog):
    def __init__(self , name , color):
        Dog.__init__(self , name , owner="GoldenRetriver")
        self.color = color

    def show(self):
        Dog.show(self)
        print(f"The color of the Animal is {self.color}")

obj = GoldenRetriver("Dog " , "White")
obj.show()
print(GoldenRetriver.mro())