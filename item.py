from cargo import Cargo
from enum import Enum



class Item(Cargo):
    class Rarity(Enum):
        common = 1
        rare = 5
        epic = 20
        legendary = 50

    def __init__(self, name: str, amount: int, base_price: int, rarity: Rarity):
        super().__init__(name, amount, base_price)
        if isinstance(rarity, Item.Rarity):
            self.__rarity = rarity
        else:
            raise TypeError('Rarity must be a Item.Rarity class instance')   

    # properties

    @property
    def rarity(self):
        return self.__rarity

    # methods

    def __repr__(self):
        return super().__repr__() + '\n' + 'Rarity: {}'.format(self.__rarity)

    def getPrice(self):
        return self.base_price * self.__rarity.value
    
    


