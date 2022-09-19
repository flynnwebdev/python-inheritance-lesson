from dataclasses import dataclass

class Currency:
    def __init__(self, gold, silver, copper):
        self.value = (gold, silver, copper)

    def __rebalance(self):
        self.__silver += self.__copper // 100
        self.__copper %= 100
        self.__gold += self.__silver // 100
        self.__silver %= 100

    @property
    def value(self):
        return self.__gold, self.__silver, self.__copper

    @value.setter
    def value(self, value_tuple):
        gold, silver, copper = value_tuple
        self.__gold = gold
        self.__silver = silver
        self.__copper = copper
        self.__rebalance()

    def __iadd__(self, other):
        if not isinstance(other, (Currency, int)):
            raise TypeError("other must be Currency or int")

        if isinstance(other, Currency):
            gold, silver, copper = other.value
        else:
            gold, silver, copper = (0, 0, other)

        self.__gold += gold
        self.__silver += silver
        self.__copper += copper
        self.__rebalance()
        return self

    def __add__(self, other):
        gold, silver, copper = other.value
        return Currency(
            self.__gold + gold,
            self.__silver + silver,
            self.__copper + copper
        )

    # Define a string representation of the object
    # Should return a Python expression that reconstructs the object
    # Intended for use by developers
    def __repr__(self):
        return f'Currency(gold={self.__gold}, silver={self.__silver}, copper={self.__copper})'

    def __str__(self):
        return f'{self.__gold}G {self.__silver}S {self.__copper}C'


class Combat:
    def __init__(self, health=100, attack=10):
        self.health = health
        self.attack = attack

    def battle(self, other):
        print(f'{self.name} launches a brutal melee attack on {other.name}!!')


@dataclass
class Character:
    __available_races = ['Human', 'Elf', 'Orc', 'Goblin', 'Dwarf']

    name: str = ''
    race: str = ''
    purse: Currency = Currency(0, 0, 0)

    @classmethod
    def is_valid_race(cls, race):
        return race in cls.__available_races


class Warrior(Character, Combat):
    def __init__(self, name, race, *, health=100, attack=30):
        Character.__init__(self)
        Combat.__init__(self, health=health, attack=attack)


class Mage(Character, Combat):
    def __init__(self, name, race, *, health=40, attack=50, mana=200):
        Character.__init__(self)
        Combat.__init__(self, health=health, attack=attack)
        self.mana = mana

    def cast(self, spell):
        self.mana -= 10

    def battle(self, other):
        print(f'{self.name} casts a wicked spell at {other.name}!!')
        self.cast('fireball')


@dataclass
class Vendor(Character):
    __inventory: list = []
    purse: Currency = Currency(1000, 0, 0)


class Chest:
    def __init__(self, items, gold, silver, copper):
        self.items = items
        self.cash = Currency(gold, silver, copper)

    # Transfer contents of this chest to character
    def loot(self, character):
        # gold, silver, copper = self.cash.value
        # character.purse.add(gold, silver, copper)
        character.purse += self.cash
        self.cash.value = (0, 0, 0)
    