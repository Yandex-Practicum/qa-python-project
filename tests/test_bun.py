import allure
import pytest

class TestBun:
    @pytest.mark.parametrize("name_expected, price_expected", [
        ("Классическая булочка", 1.5),
        ("Сырная булочка", 2.0),
        ("Острая булочка", 1.75),
    ])
    @allure.title("Проверка установки имени и прайса для булочки")
    def test_bun_properties(self, bun_fixture, name_expected, price_expected):
        bun_fixture.name = name_expected
        bun_fixture.price = price_expected
        assert bun_fixture.get_name() == name_expected
        assert bun_fixture.get_price() == price_expected

    @allure.title("Проверка метода get_name")
    def test_get_name(self, bun_fixture):
        bun_fixture.name = "Классическая булочка"
        assert bun_fixture.get_name() == "Классическая булочка"

    @allure.title("Проверка метода get_price")
    def test_get_price(self, bun_fixture):
        bun_fixture.price = 1.5
        assert bun_fixture.get_price() == 1.5
