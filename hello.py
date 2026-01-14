class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"

    def __str__(self):
        return f"Dog named {self.name}"

    def __repr__(self):
        return f"Dog(name='{self.name}', breed='{self.breed}')"


class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color


jerry = Dog("Jerry", "Beagle")

print(jerry)
print(jerry.bark())


class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age
    
    def info(self):
        return f"{self.species}, Age: {self.age}"

class Bird(Animal):
    def __init__(self, species, age, can_fly):
        super().__init__(species, age)
        self.can_fly = can_fly
    
    def info(self):
        fly_status = "can fly" if self.can_fly else "cannot fly"
        return f"{super().info()}, {fly_status}"

parrot = Bird("Parrot", 2, True)
print(parrot.info())