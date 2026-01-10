import pytest

from practicum.ingredient import Ingredient
import practicum.ingredient_types as indegrient_types
import test_data


class TestIngredient:
    @pytest.mark.parametrize('ingredient', test_data.INGREDIENT_CORRECT_SET, indirect=True)
    def test_get_name(self, ingredient):
        # Проверка метода get_name
        assert isinstance(ingredient.get_name(), str), "Имя может быть только строкой"

    @pytest.mark.parametrize('ingredient', test_data.INGREDIENT_CORRECT_SET, indirect=True)
    def test_get_price(self, ingredient):
        # Проверка метода get_price
        assert isinstance(ingredient.get_price(), float) or isinstance(ingredient.get_price(), int), ("Цена может "
                                                                                                      "принимать "
                                                                                                      "только "
                                                                                                      "числовое "
                                                                                                      "значение")

    @pytest.mark.parametrize('ingredient', test_data.INGREDIENT_CORRECT_SET, indirect=True)
    def test_get_type(self, ingredient):
        # Проверка метода get_type
        assert isinstance(ingredient.get_type(), str), "Тип ингридиента может быть только строкой!"
        assert ingredient.get_type() in [indegrient_types.INGREDIENT_TYPE_SAUCE,
                                         indegrient_types.INGREDIENT_TYPE_FILLING], ("Тип ингридиента только 'SAUCE' "
                                                                                     "или 'FILLING'")

    @pytest.mark.parametrize('ingredient', test_data.INGREDIENT_CORRECT_SET, indirect=True)
    def test_ingredient_initialization(self, ingredient):
        # Проверка инициализации объекта Ingredient
        assert ingredient.get_name() in ["Mayonnaise", "Филе курицы", "Ketchup_1"], ("Ошибка при инициализации поля "
                                                                                     "name объекта Ingredient")
        assert ingredient.get_price() in [15, 150.0, 75.5], "Ошибка при инициализации поля price объекта Ingredient"
        assert ingredient.get_type() in [indegrient_types.INGREDIENT_TYPE_SAUCE,
                                         indegrient_types.INGREDIENT_TYPE_FILLING], ("Ошибка при инициализации поля "
                                                                                     "type объекта Ingredient")

    @pytest.mark.parametrize('ingredient', test_data.INGREDIENT_INCORRECT_SET, indirect=True)
    def test_ingredient_wrong_type_initialization(self, ingredient):
        # Проверка на отсутствие инициализации объекта Ingredient при некорректных значениях
        assert ingredient.get_name() not in [None, 123], "Имя инициализируется неверным типом"
        assert ingredient.get_price() not in [None, "100", [1, 2], {"1": 1.0, "2": 2}], ("Цена инициализируется "
                                                                                         "неверным типом")
        assert ingredient.get_type() not in [None], "Поле тип инициализируется неверным типом"

    def test_price_non_negative(self):
        # Проверка, что цена не может быть отрицательной или нулевой в рамках верного типа
        with pytest.raises(ValueError):
            Ingredient(ingredient_type=indegrient_types.INGREDIENT_TYPE_SAUCE, name="Тест", price=-5.0), ("Цена не "
                                                                                                          "может "
                                                                                                          "принимать "
                                                                                                          "отрицательное значение")
        with pytest.raises(ValueError):
            Ingredient(ingredient_type=indegrient_types.INGREDIENT_TYPE_SAUCE, name="Тест", price=0), ("Цена не может "
                                                                                                       "быть нулевой")

    def test_invalid_ingredient_type(self):
        # Проверка на создание ингредиента с неизвестным типом
        with pytest.raises(ValueError):
            Ingredient(ingredient_type="UNKNOWN_INGREDIENT_TYPE", name="Неизвестный", price=10.0), ("Тип ингридиента "
                                                                                                    "может только "
                                                                                                    "'SAUCE' или "
                                                                                                    "'FILLING'")

    def test_name_non_empty(self):
        # Проверка, что имя не может быть пустым в рамках верного типа
        with pytest.raises(ValueError):
            Ingredient(ingredient_type=indegrient_types.INGREDIENT_TYPE_SAUCE, name="", price=10.0), ("Имя не может "
                                                                                                      "быть пустым!")
