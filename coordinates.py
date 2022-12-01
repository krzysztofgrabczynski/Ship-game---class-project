from random import randint


class Coordinates:

    list_of_used_coordinates = []

    def random_cords(self):
        while True:
            cord = (0,0)
            cord.x = randint(0, 400)
            cord.y = randint(0, 400)
            if not cord in self.list_of_used_coordinates:
                self.list_of_used_coordinates.append(cord)
                break
        return cord

    def __init__(self):
        self.__x = self.random_cords().x
        self.__y = self.random_cords().y


    # properties

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
        