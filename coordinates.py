from random import randint


class Coordinates:

    __list_of_used_coordinates = []

    def random_cords(self):
        while True:
            x = randint(0, 400)
            y = randint(0, 400)
            cord = (x, y)
            if not cord in self.__list_of_used_coordinates:
                self.__list_of_used_coordinates.append(cord)
                print(cord, x, y)
                break
        return cord

    def __init__(self):
        self.__x = self.random_cords()[0]
        self.__y = self.random_cords()[1]


    # properties

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
        
cord = Coordinates()
print(vars(cord))