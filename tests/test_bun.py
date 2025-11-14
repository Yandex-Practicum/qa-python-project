import pytest
import allure
from prakticum.bun import Bun


class TestBun:
    @allure.title('Проверяем конструктор __init__() и методы get_name и get_price для разных значений')
    @pytest.mark.parametrize(
        "name, price, expected_name, expected_price",
        [
            ("Сезам", 2.5, "Сезам", 2.5),
            ("Бриошь", 3.0, "Бриошь", 3.0),
            ("", 2.0, "", 2.0),
            ("Пита", -5.0, "Пита", -5.0),
            ("$%#@", 1.5, "$%#@", 1.5),
        ]
    )
    def test_init_and_getters(self, name, price, expected_name, expected_price):
        bun = Bun(name, price)
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    @allure.title('Проверяем метод get_name() при передаче нестрокового значения')
    def test_get_name_returns_as_is(self):
        bun = Bun(12345, 4.2)  # не строка
        name = bun.get_name()
        assert name == 12345
        assert type(name) is int

    @allure.title('Проверяем метод get_price() при передаче строки вместо числа')
    def test_get_price_accepts_string(self):
        bun = Bun("Булочка", "5.5")  # строка вместо float
        price = bun.get_price()
        assert price == "5.5"
        assert type(price) is str

    @allure.title('Проверяем метод get_price() при передаче целого числа вместо float')
    def test_get_price_with_int(self):
        bun = Bun("Классическая", 5)
        price = bun.get_price()
        assert price == 5
        assert type(price) is int

    @allure.title('Проверяем метод get_price() при передаче значения типа float')
    def test_get_price_with_float(self):
        bun = Bun("Чиабатта", 5.0)
        price = bun.get_price()
        assert price == 5.0
        assert type(price) is float

    @allure.title('Проверяем работу с отрицательной ценой')
    def test_negative_price(self):
        bun = Bun("Пита", -5)
        assert bun.get_name() == "Пита"
        assert bun.get_price() == -5

    @allure.title('Проверяем работу с пустым именем булочки')
    def test_empty_name(self):
        bun = Bun("", 2.0)
        assert bun.get_name() == ""
        assert bun.get_price() == 2.0

    @allure.title('Проверяем работу с именем, состоящим из спецсимволов')
    def test_special_characters_in_name(self):
        bun = Bun("$%#@", 4.0)
        assert bun.get_name() == "$%#@"
        assert bun.get_price() == 4.0

