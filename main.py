# from person import Person

# p1 = Person(name='John', age=40)
# p2 = Person('Mary', 35)

# # p1.name = 'John'
# # print(p1)
# p1.greet()
# p2.greet()

# print(dir(p1))
# print(dir(p2))

import rpg

conan = rpg.Warrior('Conan', 'Human')
conan.purse.value = (5, 25, 0)
galadriel = rpg.Mage('Galadriel', 'Elf')
galadriel.purse.value = (10, 99, 250)
grok = rpg.Warrior('Grok', 'Orc', health=130)
chest = rpg.Chest(['longsword', 'iron helmet'], 2, 50, 25)

belethor = rpg.Vendor('Belethor', 'Human')

print(belethor)
# grok.battle(conan)

# print(galadriel.purse + conan.purse)
# print(galadriel.purse.sum(conan.purse))
# conan.battle(galadriel)
# galadriel.battle(grok)

# galadriel.purse.__gold = 2000

# print(conan.__dict__)
# print(galadriel.__dict__)
# print(grok.__dict__)

# rpg.Character.available_races.append('Ogre')
# print(rpg.Character.is_valid_race('Troll'))
# galadriel.purse.value = (20, 10, 5)
# g, s, c = galadriel.purse.value
# print(f'{galadriel.name} has {g} gold.')

# try:
#     conan.purse += "Hello"
# except TypeError:
#     print("Can't add a string to Currency!")


# galadriel.purse += 5000
# chest.loot(galadriel)

# print(chest.__dict__)
# print(galadriel.__dict__)

# print(chest.cash)
# print(f'{galadriel.name} has {galadriel.purse} in her pocket')

