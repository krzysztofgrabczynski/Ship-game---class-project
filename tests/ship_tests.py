import pytest
from sys import path
path.append(r'C:\Users\kgrab\OneDrive\Pulpit\Python\Klasy\class_ship_game')
from ship import Ship
from fruit import Fruit


class TestsShip:
    @pytest.fixture
    def ship(self):
        ship = Ship(1, 'Statek_1', 5, 10, 10) 
        return ship

    def test_ship_speed_setter_with_correct_value(self, ship):
        ship.speed = 10
        assert ship.speed == 10
    def test_ship_speed_setter_with_incorrect_value(self, ship):
        with pytest.raises(ValueError):  
            ship.speed = -1

    def test_ship_max_crew_setter_with_correct_value(self, ship):
        ship.max_crew = 10
        assert ship.max_crew == 10
    def test_ship_max_crew_setter_with_incorrect_value_v1(self, ship):
        with pytest.raises(ValueError):  
            ship.max_crew = -1  
    def test_ship_max_crew_setter_with_incorrect_value_v2(self, ship):
        with pytest.raises(ValueError):  
            ship.max_crew = 8.5

    def test_ship_adding_crew_with_correct_value(self, ship):
        ship.max_crew = 20
        ship += 15
        assert ship.crew == 15
    def test_ship_adding_crew_with_incorrect_value(self, ship): 
        ship.max_crew = 5
        with pytest.raises(ValueError):  
            ship += 30
    def test_ship_subtracting_crew_with_correct_value(self, ship):
        ship += 10
        ship -= 5
        assert ship.crew == 5
    def test_ship_subtracting_crew_with_incorrect_value(self, ship): 
        with pytest.raises(ValueError):  
            ship -= 15

    def test_ship_lack_of_space_available(self, ship):
        fruit = Fruit('banan', 100, 20)
        with pytest.raises(ValueError):
            ship.load(fruit)
    def test_ship_load_and_unload_cargo(self, ship):
        fruit_1 = Fruit('banan', 2, 20)
        fruit_2 = Fruit('jablko', 3, 20)
        ship.load(fruit_1)
        ship.load(fruit_2)
        assert len(ship.cargo) == 2
        ship.unload(1) 
        assert len(ship.cargo) == 1