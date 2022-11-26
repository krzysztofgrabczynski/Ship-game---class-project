import pytest
from sys import path
path.append(r'C:\Users\kgrab\OneDrive\Pulpit\Python\Klasy\class_ship_game')
from ship import Ship

class TestsShip:
    def test_ship_speed_setter_with_correct_value(self):
        ship = Ship(1, 'Statek_1', 5, 10, 10) 
        ship.speed = 10
        assert ship.speed == 10
    def test_ship_speed_setter_with_incorrect_value(self):
        ship = Ship(1, 'Statek_1', 5, 10, 10)
        with pytest.raises(ValueError):  
            ship.speed = -1

    def test_ship_max_crew_setter_with_correct_value(self):
        ship = Ship(1, 'Statek_1', 5, 10, 10) 
        ship.max_crew = 10
        assert ship.max_crew == 10
    def test_ship_max_crew_setter_with_incorrect_value_v1(self):
        ship = Ship(1, 'Statek_1', 5, 10, 10) 
        with pytest.raises(ValueError):  
            ship.max_crew = -1  
    def test_ship_max_crew_setter_with_incorrect_value_v2(self):
        ship = Ship(1, 'Statek_1', 5, 10, 10)
        with pytest.raises(ValueError):  
            ship.max_crew = 8.5

    def test_ship_adding_crew_with_correct_value(self):
        ship = Ship(1, 'Statek_1', 5, 10, 10) 
        ship.max_crew = 20
        ship += 15
        assert ship.crew == 15
    def test_ship_adding_crew_with_incorrect_value(self):
        ship = Ship(1, 'Statek_1', 5, 10, 10) 
        ship.max_crew = 5
        with pytest.raises(ValueError):  
            ship += 30
    def test_ship_subtracting_crew_with_correct_value(self):
        ship = Ship(1, 'Statek_1', 5, 20, 10) 
        ship += 20
        ship -= 15
        assert ship.crew == 5
    def test_ship_subtracting_crew_with_incorrect_value(self):
        ship = Ship(1, 'Statek_1', 5, 10, 10) 
        with pytest.raises(ValueError):  
            ship -= 15