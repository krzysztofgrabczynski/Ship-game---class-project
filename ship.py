from coordinates import Coordinates


class Ship:
    def __init__(self, id: int, name: str, speed: int=1, max_crew: int=1, 
                 capacity: int=1, coordinates: Coordinates=Coordinates()):
        self.__id = id
        self.__name = name
        self.__speed = speed
        self.__max_crew = max_crew
        self.__capacity = capacity
        self.__crew = 0
        self.__coordinates = coordinates

        self.__cargo = []
        self.__filled_capacity = 0

    # properties
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, value):
        if value > 0:
            self.__speed = value  
        else: 
            raise ValueError("Speed must be positive value")
            
    @property
    def max_crew(self):
        return self.__max_crew
    @max_crew.setter
    def max_crew(self, value):
        if value > 0 and isinstance(value, int):
            self.__max_crew = value
        else:
            raise ValueError("Max crew must be positive integer value")
        
    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, value):
        if value > 0:
            self.__capacity = value
        else:
            raise ValueError("Capacity must be positive value")

    @property
    def crew(self):
        return self.__crew

    @property
    def cargo(self):
        return self.__cargo

    @property
    def filled_capacity(self):
        return self.__filled_capacity

    @property
    def coordinates(self):
        return self.__coordinates

    # methods

    def __repr__(self):
        return f"Ship: {self.__name}\nSpeed: {self.__speed}\nCrew: {self.__crew}\nMax crew: {self.__max_crew}\nCapacity: {self.__capacity}"

    def __iadd__(self, other):
        if self.__crew + other <= self.__max_crew:
            self.__crew += other
            return self
        else:
            raise ValueError("Crew can't be greater than max_crew (max_crew = {})".format(self.__max_crew))
    def __isub__(self, other):
        if self.__crew - other > 0:
            self.__crew -= other
            return self
        else:
            raise ValueError("Crew can't be less than 0 (crew = {})".format(self.__max_crew))


    def __get_available_capacity(self, cargo):
        if self.__capacity <= self.__filled_capacity or cargo.amount > self.__capacity:
            #print(f'Lack of space available on ship: {self.__name}')
            raise ValueError(f"Lack of space available on ship: {self.__name}")
        else:
            return self.__capacity - self.__filled_capacity

    def load(self, cargo):
        if self.__get_available_capacity(cargo) >= cargo.amount:
            self.cargo.append(cargo)
            self.__filled_capacity += cargo.amount

    def unload(self, cargo_index: int):
        removed_cargo = self.cargo.pop(cargo_index)
        print(f'Removed cargo: {removed_cargo}')