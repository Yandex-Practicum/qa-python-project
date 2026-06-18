import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize(
        'type_, name, price',
        [
            ('Соус', 'Соус Spicy-X', 90),
            ('Начинка', 'Говяжий метеорит (отбивная)', 3000),
        ],
    )
    def test_ingredient_type_field_is_set_correctly(self, type_, name, price):
        ingredient = Ingredient(type_, name, price)

        assert ingredient.type == type_

    @pytest.mark.parametrize(
        'type_, name, price',
        [
            ('Соус', 'Соус Spicy-X', 90),
            ('Начинка', 'Говяжий метеорит (отбивная)', 3000),
        ],
    )
    def test_ingredient_name_field_is_set_correctly(self, type_, name, price):
        ingredient = Ingredient(type_, name, price)

        assert ingredient.name == name

    @pytest.mark.parametrize(
        'type_, name, price',
        [
            ('Соус', 'Соус Spicy-X', 90),
            ('Начинка', 'Говяжий метеорит (отбивная)', 3000),
        ],
    )
    def test_ingredient_price_field_is_set_correctly(self, type_, name, price):
        ingredient = Ingredient(type_, name, price)

        assert ingredient.price == price

    @pytest.mark.parametrize(
        'type_, name, price',
        [
            ('Соус', 'Соус Spicy-X', 90),
            ('Начинка', 'Говяжий метеорит (отбивная)', 3000),
        ],
    )
    def test_get_type_returns_correct_value(self, type_, name, price):
        ingredient = Ingredient(type_, name, price)

        assert ingredient.get_type() == type_

    @pytest.mark.parametrize(
        'type_, name, price',
        [
            ('Соус', 'Соус Spicy-X', 90),
            ('Начинка', 'Говяжий метеорит (отбивная)', 3000),
        ],
    )
    def test_get_name_returns_correct_value(self, type_, name, price):
        ingredient = Ingredient(type_, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        'type_, name, price',
        [
            ('Соус', 'Соус Spicy-X', 90),
            ('Начинка', 'Говяжий метеорит (отбивная)', 3000),
        ],
    )
    def test_get_price_returns_correct_value(self, type_, name, price):
        ingredient = Ingredient(type_, name, price)

        assert ingredient.get_price() == price