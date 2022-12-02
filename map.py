from random import randint
from island import Island
from store import Store


class Map:
    
    __list_of_islands = []

    def __random_island(self, min_island_number, max_island_number) -> None:
        number_of_islands = randint(min_island_number, max_island_number)

        for i in range(number_of_islands):
            self.__list_of_islands.append(Island(f'Island_{i+1}', Store(f'Store_{i+1}')))
            self.__list_of_islands[i].store.get_random_cargo()
        
    def __init__(self, min_island_number, max_island_number) -> None:
        self.__random_island(min_island_number, max_island_number)


    # properties

    @property
    def list_of_islands(self):
        return self.__list_of_islands