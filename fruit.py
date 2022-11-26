from cargo import Cargo


class Fruit(Cargo):
    def __init__(self, name, amount, base_price):
        super().__init__(name, amount, base_price)
        self.__expire_date = 10
        self.__rotten_time = self.__expire_date
        
    def __sub__(self, other):
        if self.__rotten_time > 0:
            self.__rotten_time -= 1
        else:
            print("{} is rotten!".format(self.name.capitalize()))

    def getPrice(self):
        return self.base_price * (self.__rotten_time / self.__expire_date)


