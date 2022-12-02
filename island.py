from coordinates import Coordinates
from store import Store
from ship import Ship


class Island:
    def __init__(self, name: str, store: Store, coordinates: Coordinates=Coordinates()):
        self.__name = name
        self.__store = store
        self.__coordinates = coordinates

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


    # methods

    def __repr__(self) -> str:
        return f'Island: {self.__name} with store: {self.store.name}\n'

    def __eq__(self, ship :Ship):
        if self.__coordinates.coords == ship.coordinates.coords:
            self.__store._Store__is_player_available = True
            print(f'You are on {self.__name} island. You can buy something in {self.__store.name} store')
        