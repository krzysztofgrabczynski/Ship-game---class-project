from ship import Ship
from alcohol import Alcohol
from fruit import Fruit
from item import Item


ship = Ship(1, 'Statek_1', 10, 30, 1000)
ship += 15
alcohol = Alcohol('Spirytus', 100, 27, 96)
fruit = Fruit('banan', 10, 5)
item = Item('miecz', 1, 20, Item.Rarity.rare)

print(ship)
print('-' * 30)
print(alcohol)
print('-' * 30)
print(fruit)
print('-' * 30)
print(item)