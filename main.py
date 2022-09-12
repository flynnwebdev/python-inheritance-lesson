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

conan = rpg.Character('Conan', 'Human')
galadriel = rpg.Mage('Galadriel', 'Elf')
galadriel.purse.set(10, 5, 1)
grok = rpg.Character('Grok', 'Orc', health=130)
chest = rpg.Chest(['longsword', 'iron helmet'], 2, 50, 25)

conan.battle(galadriel)
galadriel.battle(grok)


print(conan.__dict__)
print(galadriel.__dict__)

# chest.loot(galadriel)

# print(chest.__dict__)
# print(galadriel.__dict__)

# print(chest.cash)
# print(f'{galadriel.name} has {galadriel.purse} in her pocket')
