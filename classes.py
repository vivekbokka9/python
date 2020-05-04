class Gamecharector:
    name = ''
    health = 0
    position = 0
    age = 0


    def __init__(self, name, position, health, age):
        self.name = name
        self.position = position
        self.health = health
        self.age = age

    def move_by(self, amount):
        self.health += amount
    def move_by(self, amount):
        self.age += amount

    def heal_self(self, by_amount):
        self.health += by_amount
        if self.health > 100:
            self.health = 100
new_charector = Gamecharector('vivek', 80, 10, 1)
print(new_charector)
print(new_charector.name)
print(new_charector.position)
print(new_charector.health)
print(new_charector.age)
