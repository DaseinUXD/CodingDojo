class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health = self.health - 1
        return self

    def run(self):
        self.health = self.health - 5
        return self

    def displayHealth(self):
        print(self.health)
        return self


animal = Animal('cute', 100)

animal.walk()
animal.walk()
animal.walk()
animal.run()
animal.run()

print(animal.name)
print(animal.displayHealth())


class Dog(Animal):
    Animal.health = 150

    def pet(self):
        self.health = self.health + 5
        return "Dog"


print(Dog.health)

fido = Dog('fido', Dog.health)
print('This is the default health')
print(fido.health)
print('Of the dog')
fido.walk()
print(fido.health)
fido.walk()
print(fido.health)
fido.walk()
print(fido.health)
fido.run()
print(fido.health)
fido.run()
print(fido.health)
fido.pet()
print('+++++++++_-_-_-_-_-_-_++++++')
print(fido.health)


class Dragon(Animal):
    Animal.health = 170

    def fly(self):
        self.health = self.health - 10
        return "Dragon"

    def displayHealth(self):
        print('I am a Dragon')
        print(self.health)
        return self

dragon = Dragon('Draco', 1313)

print(dragon.displayHealth())

print(dragon.name)
dragon.fly()
print(dragon.displayHealth())


class Bear(Animal):
    Animal.health = 200

    def eatHoney(self):
        Animal.health = Animal.health + 5
        return "Bear"
    def myHealth(self):
        print(Animal.health)


kodiak = Bear('griz', Bear.health)
kodiak.displayHealth()
# kodiak.pet()
# kodiak.fly()
kodiak.walk()
kodiak.run()
kodiak.displayHealth()

