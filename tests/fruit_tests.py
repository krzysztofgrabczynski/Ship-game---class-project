import pytest
from sys import path
path.append(r'C:\Users\kgrab\OneDrive\Pulpit\Python\Klasy\class_ship_game')
from fruit import Fruit


class TestsFruit:
    def test_fruit_changing_amount(self):
        fruit = Fruit('apple', 2, 10)
        fruit += 1
        assert fruit.amount == 3
        fruit -= 2
        assert fruit.amount == 1

    def test_fruit_substracting_rotten_time(self):
        fruit = Fruit('apple', 2, 10)
        fruit._Fruit__rotten_time = 2
        fruit._Fruit__expire_date = 2
        
        fruit - 1
        assert fruit._Fruit__rotten_time == 1
        fruit - 1
        assert fruit._Fruit__rotten_time == 0
