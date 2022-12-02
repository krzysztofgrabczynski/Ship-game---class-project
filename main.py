from ship import Ship
from alcohol import Alcohol
from fruit import Fruit
from item import Item
from cargo import Cargo
from store import Store
from player import Player


ship = Ship(1, 'Statek_1', 10, 30, 1000)
ship += 15
alcohol = Alcohol('Spirytus', 100, 27, 96)
fruit = Fruit('banan', 10, 5)
item = Item('miecz', 1, 20, Item.Rarity.rare)
player = Player('Krzysztof', ship, 1000)

# print(ship)
# print('-' * 30)
# print(alcohol)
# print('-' * 30)
# print(fruit)
# print('-' * 30)
# print(item)
# print('-' * 30)

# ship.load(alcohol)
# ship.load(fruit)
# print(player.ship.cargo)
# print('-' * 30)

# store = Store('Sklep_1')
# store._add_cargo(Item('miecz', 10, 50, Item.Rarity.common))
# store._add_cargo(Item('tarcza', 2, 20, Item.Rarity.rare))
# print('Printowanie store przed kupowaniem', store)
# print('-' * 30)
# print('Printowanie money przed kupowaniem', player.money)
# print('-' * 30)

# store.buy(Item('miecz', 10, 50, Item.Rarity.common), player)
# print('Printowanie store po kupowaniem', store)
# print(30*'-')
# print('Printowanie money po kupowaniem', player.money)
# print(30*'-')
# print(30*'-')
# print(ship.cargo)

print(ship.coordinates)
print(player.ship.coordinates.x)
print(ship.coordinates.x)
