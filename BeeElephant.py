class PheloSlon:
    def __init__(self, bee, elephant):
        self.bee = min(100, max(0, bee))
        self.elephant = min(100, max(0, elephant))

    def fly(self):
        if self.bee >= self.elephant:
            return True
        else:
            return False

    def trumpet(self):
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.elephant -= value
            self.bee = min(100, max(0, self.bee + value))
        elif meal == "grass":
            self.bee -= value
            self.elephant = min(100, max(0, self.elephant + value))

pheloslon = PheloSlon(30, 70)
print(pheloslon.fly())
print(pheloslon.trumpet())
pheloslon.eat("nectar", 20)
print(f"Bee: {pheloslon.bee}, Elephant: {pheloslon.elephant}")