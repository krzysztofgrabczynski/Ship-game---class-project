from ship import Ship
from alcohol import Alcohol
from fruit import Fruit
from item import Item
from cargo import Cargo
from store import Store
from player import Player
from map import Map


#####################################
############# GAME BODY #############
#####################################

# bilding map with islands
map = Map(3, 8)         
print('\n\n', 100*'#', '\n', 'List of islands:\n', map.list_of_islands)
print(100*'#', '\n', 'Coordinates of first island:\n', map.list_of_islands[0].coordinates)
print(100*'#', '\n', 'Coordinates of second island:\n', map.list_of_islands[1].coordinates)
print(100*'#', '\n', 'Inventory in the store on second island:\n',map.list_of_islands[1].store)
print('\n')
# creating player with specific ship
player = Player('Jon', Ship(1, 'Victory', 200, 100, 1000), 5000)
print(100*'#', '\n', 'Player name and money amount: ', player.name, player.money)
print(100*'#', '\n', f"Player's ship name: {player.ship.name}, speed: {player.ship.speed}, max crew: {player.ship.max_crew}, capacity: {player.ship.capacity}\n")
# adding crew into player's ship
player.ship += 80
print(100*'#', '\n', f"Player's ship crew: {player.ship.crew}\n"),
print(100*'#', '\n', "Player's ship coordinates: ", player.ship.coordinates)
# adding cargo into player's ship
fruit = Fruit('apple', 40, 5)
player.ship.load(fruit)
print(100*'#', '\n', "Player's ship cargo: \n", player.ship.cargo)
# checking rotten time of fruit
print(100*'#', '\n', f"Rotten time of {fruit.name} before substracting: ", fruit.rotten_time)
fruit - 1
print(f"Rotten time of {fruit.name} after substracting: ", fruit.rotten_time)
# checking distance between ship and first island
print(100*'#', '\n', f"Ship coordinates: {player.ship.coordinates} and first island coordiantes: {map.list_of_islands[0].coordinates}")
print("Distance: ", player.ship.coordinates.distance(map.list_of_islands[0].coordinates))



#####################################
########### GAME BODY END ###########
#####################################



### TESTS ###

# ship = Ship(1, 'Statek_1', 10, 30, 1000)
# ship += 15
# alcohol = Alcohol('Spirytus', 100, 27, 96)
# fruit = Fruit('banan', 10, 5)
# item = Item('miecz', 1, 20, Item.Rarity.rare)
# player = Player('Krzysztof', ship, 1000)

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

# print(ship.coordinates)
# print(player.ship.coordinates.x)
# print(ship.coordinates.x)
