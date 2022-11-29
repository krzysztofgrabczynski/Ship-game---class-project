from abc import ABC, abstractmethod


class Cargo(ABC):
    def __init__(self, name: str, amount: int, base_price: int):
        self.__name = name
        self.__amount = amount
        self.__base_price = base_price

    # properties

    @property
    def name(self):
        return self.__name
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def base_price(self):
        return self.__base_price

    # methods
    
    def __repr__(self):
        return f"Cargo: {self.name}\nAmount: {self.amount}\nBase price: {self.base_price}"

    def __iadd__(self, other):
        self.__amount += other
        return self
    def __isub__(self, other):
        if self.__amount - other < 0:
            self.__amount = 0
        else:
            self.__amount -= other  
        return self
    def __eq__(self, other):
        return self.__name == other.name and self.__amount == other.amount and self.__base_price == other.base_price
    
    @abstractmethod
    def getPrice(self):
        pass