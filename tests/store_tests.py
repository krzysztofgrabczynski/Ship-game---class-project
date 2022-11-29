import pytest
from sys import path
path.append(r'C:\Users\kgrab\OneDrive\Pulpit\Python\Klasy\class_ship_game')
from ship import Ship
from alcohol import Alcohol
from fruit import Fruit
from item import Item
from cargo import Cargo
from store import Store
from player import Player


class TestsStore:
    def test_store_get_random_cargo_function(self):
        store = Store('Sklep_1')
        store.get_random_cargo()
        store.get_random_cargo()
        assert len(store.cargo) == 2
        assert isinstance(store.cargo[0], Cargo)
        assert isinstance(store.cargo[1], Cargo)
    def test_store_add_cargo_function(self):
        store = Store('Sklep_1')
        store._add_cargo(Item('miecz', 10, 50, Item.Rarity.common))
        assert len(store.cargo) == 1
        assert isinstance(store.cargo[0], Cargo)
    def test_store_buy_option_positive(self):
        ship = Ship(1, 'Statek_1', 5, 10, 1000)
        player = Player('Krzysztof', ship, 1000)
        store = Store('Sklep_1')

        store._add_cargo(Item('miecz', 10, 50, Item.Rarity.common))
        cargo_to_buy = Item('miecz', 10, 50, Item.Rarity.common)
        store.buy(cargo_to_buy, player)
        price = cargo_to_buy.amount * cargo_to_buy.getPrice()

        assert player.money == 1000 - price
        assert len(store.cargo) == 0
        assert len(player.ship.cargo) == 1
    def test_store_buy_option_negative_lack_of_cargo(self):
        ship = Ship(1, 'Statek_1', 5, 10, 1000)
        player = Player('Krzysztof', ship, 1000)
        store = Store('Sklep_1')

        cargo_to_buy = Item('miecz', 10, 50, Item.Rarity.common)
        with pytest.raises(ValueError):
            store.buy(cargo_to_buy, player)
    def test_store_buy_option_negative_lack_of_money(self):
        ship = Ship(1, 'Statek_1', 5, 10, 1000)
        player = Player('Krzysztof', ship, 0)
        store = Store('Sklep_1')

        store._add_cargo(Item('miecz', 10, 50, Item.Rarity.common))
        cargo_to_buy = Item('miecz', 10, 50, Item.Rarity.common)
        store.buy(cargo_to_buy, player)
        assert player.money == 0
        assert len(store.cargo) == 1
        assert len(player.ship.cargo) == 0
    def test_store_buy_option_negative_lack_of_space_v1(self):
        ship = Ship(1, 'Statek_1', 5, 10, 0)
        player = Player('Krzysztof', ship, 1000)
        store = Store('Sklep_1')

        store._add_cargo(Item('miecz', 10, 50, Item.Rarity.common))
        cargo_to_buy = Item('miecz', 10, 50, Item.Rarity.common)
        store.buy(cargo_to_buy, player)
        assert player.money == 1000
        assert len(store.cargo) == 1
        assert len(player.ship.cargo) == 0
