import pytest
import allure
from unittest.mock import Mock
from praktikum.bun import Bun

class TestBun:

    @allure.title("Проверка получение названия булочки")
    @pytest.mark.parametrize("test_name", [
        "Classic Bun",
        "Special Edition",
    ])
    def test_get_name(self, test_name):
        bun = Bun(test_name, 50.0)
        assert bun.get_name() == test_name

    @allure.title("Проверка с использованием мока для метода get_price")
    def test_mock_get_price(self):
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = 200.5
        assert mock_bun.get_price() == 200.5    

    @allure.title("Проверка на создание булочки с правильными именем, ценой и разными данными")     
    @pytest.mark.parametrize("name,price", [
        ("Black Bun", 100.0),
        ("White Bun", 80.5),
        ("Gluten-Free Bun", 777.77),
        ("", 0.0)
    ])
    def test_bun_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name and bun.get_price() == price