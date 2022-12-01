class Island:
    def __init__(self, name, coordinates):
        self.__name = name
        self.__coordinates = coordinates
        self.__coordinates_x = coordinates.x
        self.__coordinates_y = coordinates.y


    # properties

    @property
    def name(self):
        return self.__name
    @property
    def coordinates(self):
        return self.__coordinates

    @property
    def coordinates_x(self):
        return self.__coordinates_x

    @property
    def coordinates_y(self):
        return self.__coordinates_y

