from cargo import Cargo


class Alcohol(Cargo):
    def __init__(self, name: str, amount: int, base_price: int, percentage: int=96):
        super().__init__(name, amount, base_price)
        self.__percentage = percentage
        self.__base_percentage = 96

    # properties

    @property
    def percentage(self):
        return self.__percentage

    # methods
    
    def __repr__(self):
        return super().__repr__() + "\n" + "Percentage: {}".format(self.__percentage)
        
    def __eq__(self, other):
        return super().__eq__(other) and self.__percentage == other.percentage 

    def getPrice(self):
        return self.base_price * (self.__percentage / self.__base_percentage)


