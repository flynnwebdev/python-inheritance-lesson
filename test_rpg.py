import pytest
from rpg import Chest, Currency, Character

@pytest.fixture
def chest():
    return Chest(items=['sword', 'helmet'], gold=10, silver=50, copper=25)

@pytest.fixture
def character():
    elrond = Character(name='Elrond', race='Elf')
    elrond.purse.value = (5, 10, 15)
    return elrond

class TestChest:
    def test_value(self, chest):
        assert isinstance(chest.cash, Currency)
        assert chest.cash.value == (10, 50, 25)

    def test_loot_method(self, chest, character):
        chest.loot(character)
        assert chest.cash.value == (0, 0, 0)
        assert character.purse.value == (15, 60, 40)
