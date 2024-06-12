class Animal:
    def __init__(self,eat,sleep,communicate):
        self.eat=eat
        self.sleep=sleep
        self.comminicate = communicate
class Dog(Animal):
    def __init__(self,bark,fetch):
        super().__init__(bark,fetch)
        self.bark=bark
        self.fetch=fetch
animal=Dog(bark=True,fetch=True)
print(animal.eat)
print(animal.sleep)
print(animal.comminicate)
print(animal.bark)
print(animal.fetch)