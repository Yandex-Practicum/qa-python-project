
class TestIngredient:

    def test_get_price(self, mock_ingredient):#Позитивный тест. Возвращает price ингредиента.
        ingredient_test = mock_ingredient.get_price()
        assert ingredient_test == 1000, f'Не верная стоимость'

    def test_get_name(self, mock_ingredient):#Позитивный тест. Возвращает name ингредиента.
        ingredient_test = mock_ingredient.get_name()
        assert ingredient_test == 'Медвежатина', f'Не верное название'


    def test_get_type(self, mock_ingredient):#Позитивный тест. Возвращает ingredient_type.
        ingredient_test = mock_ingredient.get_type()
        assert ingredient_test == 'Начинка', f'Не верный тип'
