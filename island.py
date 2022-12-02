from coordinates import Coordinates
from store import Store


class Island:
    def __init__(self, name: str, store: Store, coordinates: Coordinates=Coordinates()):
        self.__name = name
        self.__store = store
        self.__coordinates = coordinates
        self.__coordinates_x = coordinates.x
        self.__coordinates_y = coordinates.y


    # properties

    @property
    def name(self):
        return self.__name

    @property
    def store(self):
        return self.__store

    @property
    def coordinates(self):
        return self.__coordinates

    @property
    def coordinates_x(self):
        return self.__coordinates_x

    @property
    def coordinates_y(self):
        return self.__coordinates_y

    # methods

    def __repr__(self) -> str:
        return f'Island: {self.__name} with store: {self.store.name}\n'