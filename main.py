from ship import Ship
from alcohol import Alcohol
from fruit import Fruit

ship = Ship(1, 'Statek_1', 10, 30, 1000)
ship += 15
alcohol = Alcohol('Spirytus', 100, 27, 96)
fruit = Fruit('banan', 10, 5)

print(ship)
print('-' * 30)
print(alcohol)
print('-' * 30)
print(fruit)