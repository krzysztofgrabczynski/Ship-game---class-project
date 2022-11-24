class Ship:
    def __init__(self, id, name, speed=1, max_crew=10, capacity=10):
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
    @property
    def speed(self):
        return self.__speed
    @property
    def max_crew(self):
        return self.__max_crew
    @property
    def capacity(self):
        return self.__capacity
    
    