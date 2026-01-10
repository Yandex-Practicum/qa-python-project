import pytest
from Diplom_1.practikum.ingredient import (Ingredient)
class TestIngridientsMethods:
    @pytest.mark.parametrize('name, price, check_output_value', [
        ('Салат', 2.50, 2.50),
        ('Мясо', 7.20, 7.20)
    ])
    def test_get_price(self, name, price, check_output_value):
        ingridient = Ingredient('Бургер', name, price)
        assert ingridient.get_price() == check_output_value

    def test_get_name(self):
        ingridient = Ingredient('Овощи', 'Салат', 2.08)
        assert ingridient.get_name() == 'Салат'

    def test_get_type(self):
        ingridient = Ingredient('Овощи', 'Салат', 2.08)
        assert ingridient.get_type() == 'Овощи'