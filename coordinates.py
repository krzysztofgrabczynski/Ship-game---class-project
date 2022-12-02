from random import randint
from math import sqrt

class Coordinates:

    __list_of_used_coordinates = []
    __map_width = 400
    __map_height = 400

    def __random_cords(self):
        while True:
            x = randint(1, self.__map_width)
            y = randint(1, self.__map_height)
            cord = (x, y)
            if not cord in self.__list_of_used_coordinates:
                self.__list_of_used_coordinates.append(cord)
                return cord
        
        
    def __init__(self):
        self.__cords = self.__random_cords()
        self.__x = self.__cords[0]
        self.__y = self.__cords[1]


    # properties

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        self.__y = new_y

    @property
    def coords(self):
        self.__cords = (self.__x, self.__y)
        return self.__cords
    
    # methods

    def __repr__(self) -> str:
        return f'Coordinates: {self.get_coordinates()}'

    def get_coordinates(self):
        return (self.__x, self.__y)

    def distance(self, other):
        return sqrt((self.__x - other.x) ** 2 + (self.__y - other.y) ** 2)



