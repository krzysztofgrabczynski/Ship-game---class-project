from ship import Ship

class Player:
    def __init__(self, name: str, ship: Ship, money: int):
        self.__name = name
        self.ship = ship
        self.__money = money

    # properties

    @property
    def name(self):
        return self.__name

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money
    