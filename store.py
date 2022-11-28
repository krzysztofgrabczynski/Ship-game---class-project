from enum import Enum

from fruit import Fruit
from alcohol import Alcohol
from item import Item
from player import Player


class Store():
    class Response(Enum):
        done = 1
        lack_of_money = 2
        lack_ofcargo = 3
        lack_of_space = 4
    
    # methods

    def 