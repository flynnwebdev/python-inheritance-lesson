class Currency:
    def __init__(self, gold, silver, copper):
        self.set(gold, silver, copper)

    def set(self, gold, silver, copper):
        self.gold = gold
        self.silver = silver
        self.copper = copper

    def add(self, gold, silver, copper):
        self.gold += gold
        self.silver += silver
        self.copper += copper

    # Define a string representation of the object
    # Should return a Python expression that reconstructs the object
    # Intended for use by developers
    def __repr__(self):
        return f'Currency(gold={self.gold}, silver={self.silver}, copper={self.copper})'

    def __str__(self):
        return f'{self.gold}G {self.silver}S {self.copper}C'


class Character:
    def __init__(self, name, race, *, health=100, attack=10):
        self.name = name
        self.race = race
        self.health = health
        self.attack = attack
        self.purse = Currency(0, 0, 0)

    def battle(self, other):
        print(f'{self.name} launches a brutal melee attack on {other.name}!!')


class Mage(Character):
    def __init__(self, name, race, *, health=40, attack=50, mana=200):
        super().__init__(name, race, health=health, attack=attack)
        self.mana = mana

    def cast(self, spell):
        self.mana -= 10

    def battle(self, other):
        print(f'{self.name} casts a wicked spell at {other.name}!!')
        self.cast('fireball')


class Chest:
    def __init__(self, items, gold, silver, copper):
        self.items = items
        self.cash = Currency(gold, silver, copper)

    # Transfer contents of this chest to character
    def loot(self, character):
        character.purse.add(self.cash.gold, self.cash.silver, self.cash.copper)
        self.cash.gold = 0
        self.cash.silver = 0
        self.cash.copper = 0

    