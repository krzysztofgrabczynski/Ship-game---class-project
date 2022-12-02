import pytest
from sys import path
path.append(r'C:\Users\kgrab\OneDrive\Pulpit\Python\Klasy\class_ship_game')
from coordinates import Coordinates


class TestsCoordinates:
    def test_coordinates_checking_distance_func(self):
        cord_1 = Coordinates()
        cord_1.x = 5
        cord_1.y = 10

        cord_2 = Coordinates()
        cord_2.x = 1
        cord_2.y = 7

        distance_1 = cord_1.distance(cord_2)
        distance_2 = cord_2.distance(cord_1)
        assert distance_1 == 5
        assert distance_2 == 5
