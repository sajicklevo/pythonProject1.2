class Vehicle:
    def __init__(self,start,stop,move):
        self.start=start
        self.stop=stop
        self.move=move
class Car(Vehicle):
    def __init__(self,start,stop,move,drive,pedal):
        super().__init__(start,stop,move)
        self.start=start
        self.stop=stop
        self.move=move
        self.drive=drive
        self.pedal=pedal
class Bicycle(Vehicle):
    def __init__(self,start,stop,move,drive,pedal):
        super().__init__(start, stop, move)
        self.start=start
        self.stop=stop
        self.move=move
        self.drive=drive
        self.pedal=pedal
car=Car(1,2,3)
print(car.start)
print(car.stop)
print(car.move)
print(car.drive)
print(car.pedal)
bicycle=Bicycle(1,2,3)
print(bicycle.start)
print(bicycle.stop)
print(bicycle.move)
print(bicycle.drive)
print(bicycle.pedal)