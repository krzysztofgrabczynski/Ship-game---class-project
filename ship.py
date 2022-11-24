class Ship:
    def __init__(self, id, name, speed=1, max_crew=1, capacity=1):
        self.__id = id
        self.__name = name
        self.__speed = speed
        self.__max_crew = max_crew
        self.__capacity = capacity

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

    @property
    def max_crew(self):
        return self.__max_crew
    @max_crew.setter
    def max_crew(self, value):
        if value > 0 and isinstance(value, int):
            return self.__max_crew == value
        
    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, value):
        if value > 0:
            return self.__capacity == value
