from abc import ABC

class Bird(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Owl(Bird):
    def __init__(self,canfly, noise, extinct):
        super().__init__('Owl')
        self.canfly = canfly
        self.noise = noise
        self.extinct = extinct

    def __repr__(self):
        return Owl


class Dodo(Bird):
    def __init__(self, canfly, noise, extinct):
        self.canfly = canfly
        self.noise = noise
        self.extinct = extinct
    
    def __repr__(self):
        return Dodo


owl1 = Owl("Steve", 2, True, "Whoo", False)
dodo1 = Dodo("Dave", 3, False, "Squawk", True)

print(f"Name:{owl1.name} Age:{owl1.age}, Can it fly?:{owl1.canfly}, What noise does it make?:{owl1.noise}, Is it extinct?: {owl1.extinct}")
print(f"Name:{dodo1.name}, Age:{dodo1.age}, Can it fly?:{dodo1.canfly}, What noise does it make?:{dodo1.canfly}, Is it extinct?: {dodo1.extinct}")


        