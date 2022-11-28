from ship import Ship
from alcohol import Alcohol
from fruit import Fruit
from item import Item
from cargo import Cargo


ship = Ship(1, 'Statek_1', 10, 30, 1000)
ship += 15
alcohol = Alcohol('Spirytus', 100, 27, 96)
fruit = Fruit('banan', 10, 5)
item = Item('miecz', 1, 20, Item.Rarity.rare)

# print(ship)
# print('-' * 30)
# print(alcohol)
# print('-' * 30)
# print(fruit)
# print('-' * 30)
# print(item)
# print('-' * 30)

ship.load(alcohol)
ship.load(fruit)
print(ship.cargo)
# print('-' * 30)
ship.unload(0)
print(ship.cargo)