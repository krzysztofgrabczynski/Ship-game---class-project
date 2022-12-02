from enum import Enum, auto
from random import randint, choice

from fruit import Fruit
from alcohol import Alcohol
from item import Item
from player import Player


class Store():
    class Response(Enum):
        done = 'Done'
        lack_of_money = 'Lack of money'
        lack_of_cargo = 'Lack of cargo'
        lack_of_space = 'Lack of space' 
    class Cargos(Enum):
        Fruit = auto()
        Alcohol = auto() 
        Item = auto()
    class Fruit_names(Enum):
        Apple = auto()
        Banana = auto()
        Orange = auto()
    class Alcohol_names(Enum):
        Spiritus = auto()
        Beer = auto()
        Rum = auto()
    class Item_names(Enum):
        Sword = auto()
        Armour = auto()
        Shield = auto()


    def __init__(self, name: str):
        self.__name = name
        self.__cargo = []

        self.__is_player_available = False

    # properties

    @property
    def cargo(self):
        return self.__cargo

    @property
    def name(self):
        return self.__name

    # methods

    def __repr__(self):
        return f'All cargo in {self.__name}:\n{self.__cargo}'

    def __get_random_Fruit(self):
        random_name = choice(list(self.Fruit_names)).name
        random_amount = randint(1,50)
        random_base_price = randint(5, 10)
        self.__cargo.append(Fruit(random_name, random_amount, random_base_price))

    def __get_random_Alcohol(self):
        random_name = choice(list(self.Alcohol_names)).name
        random_amount = randint(1,20)
        random_base_price = randint(20, 50)
        random_percentage = randint(40, 96)
        self.__cargo.append(Alcohol(random_name, random_amount, random_base_price, random_percentage))

    def __get_random_Item(self):
        random_name = choice(list(self.Item_names)).name
        random_amount = randint(1,5)
        random_base_price = randint(40, 100)
        random_rarity = choice(list(Item.Rarity))
        self.__cargo.append(Item(random_name, random_amount, random_base_price, random_rarity))

    def get_random_cargo(self):
        random_cargo = choice(list(self.Cargos))

        if random_cargo.name == 'Fruit':
            self.__get_random_Fruit()
        if random_cargo.name == 'Alcohol':
            self.__get_random_Alcohol()
        if random_cargo.name == 'Item':
            self.__get_random_Item()

    def _add_cargo(self, cargo):
        self.__cargo.append(cargo)

    def __enought_money(self, player, cargo):
        return player.money >=  cargo.amount * cargo.getPrice()

    def __enought_space(self, player, cargo):
        return player.ship.capacity - player.ship.filled_capacity >= cargo.amount

    def __substracting_players_money(self, player, cargo):
        player.money -=cargo.amount * cargo.getPrice() 

    def buy(self, cargo_to_buy, player: Player):
        if not self.__is_player_available:
            raise AttributeError('Player is not on specific island with this store')
        if cargo_to_buy in self.__cargo:
            if not self.__enought_money(player, cargo_to_buy):
                print(self.Response.lack_of_money) 

            elif not self.__enought_space(player, cargo_to_buy):
                print(self.Response.lack_of_space)
            
            else:
                print(self.Response.done)
                self.__substracting_players_money(player, cargo_to_buy)
                self.__cargo.remove(cargo_to_buy)
                player.ship.load(cargo_to_buy)
        else:
            print(self.Response.lack_of_cargo)
            raise ValueError("Cargo to buy not available in store inventory")

    def sell(self, cargo_to_sell, player):
        pass




