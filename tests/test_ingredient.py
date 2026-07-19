import pytest
from ingredient import Ingredient
from testdata.data_ingredient import (
    INGREDIENT_VALID_DATA,
    INGREDIENT_BOUNDARY_TYPES,
    INGREDIENT_BOUNDARY_NAMES,
    INGREDIENT_BOUNDARY_PRICES,
    INGREDIENT_COMBINED_DATA,
)


class TestIngredientValid:
    """Тесты корректного создания и работы ингредиента."""

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_type, expected_name, expected_price",
        INGREDIENT_VALID_DATA,
    )
    def test_constructor_valid_data_stores_correctly(
        self, ingredient_type, name, price,
        expected_type, expected_name, expected_price,
    ):
        """
        Given: тип, имя и цена ингредиента
        When: создаем объект Ingredient
        Then: атрибуты сохраняются корректно
        """
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.type == expected_type
        assert ingredient.name == expected_name
        assert ingredient.price == expected_price

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_type, expected_name, expected_price",
        INGREDIENT_VALID_DATA,
    )
    def test_get_type_valid_type_returns_type(
        self, ingredient_type, name, price,
        expected_type, expected_name, expected_price,
    ):
        """
        Given: ингредиент с заданными значениями
        When: вызываем get_type
        Then: геттер возвращает корректное значение
        """
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == expected_type

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_type, expected_name, expected_price",
        INGREDIENT_VALID_DATA,
    )
    def test_get_name_valid_name_returns_name(
        self, ingredient_type, name, price,
        expected_type, expected_name, expected_price,
    ):
        """
        Given: ингредиент с заданными значениями
        When: вызываем get_name
        Then: геттер возвращает корректное значение
        """
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == expected_name

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_type, expected_name, expected_price",
        INGREDIENT_VALID_DATA,
    )
    def test_get_price_valid_price_returns_price(
        self, ingredient_type, name, price,
        expected_type, expected_name, expected_price,
    ):
        """
        Given: ингредиент с заданными значениями
        When: вызываем get_price
        Then: геттер возвращает корректное значение
        """
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == expected_price

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [(d[0], d[1], d[2]) for d in INGREDIENT_VALID_DATA],
    )
    def test_get_type_valid_type_returns_str(self, ingredient_type, name, price):
        """
        Given: ингредиент
        When: вызываем get_type
        Then: геттер возвращает str
        """
        ingredient = Ingredient(ingredient_type, name, price)

        assert isinstance(ingredient.get_type(), str)

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [(d[0], d[1], d[2]) for d in INGREDIENT_VALID_DATA],
    )
    def test_get_name_valid_name_returns_str(self, ingredient_type, name, price):
        """
        Given: ингредиент
        When: вызываем get_name
        Then: геттер возвращает str
        """
        ingredient = Ingredient(ingredient_type, name, price)

        assert isinstance(ingredient.get_name(), str)

    @pytest.mark.unit
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [(d[0], d[1], d[2]) for d in INGREDIENT_VALID_DATA],
    )
    def test_get_price_valid_price_returns_number(self, ingredient_type, name, price):
        """
        Given: ингредиент
        When: вызываем get_price
        Then: геттер возвращает число
        """
        ingredient = Ingredient(ingredient_type, name, price)

        assert isinstance(ingredient.get_price(), (int, float))


class TestIngredientBoundary:
    """Тесты граничных значений и нестандартных входных данных."""

    @pytest.mark.unit
    @pytest.mark.parametrize("ingredient_type", INGREDIENT_BOUNDARY_TYPES)
    def test_get_type_boundary_value_stores_correctly(self, ingredient_type):
        """
        Given: граничное значение типа
        When: создаем ингредиент
        Then: тип сохраняется без изменений
        """
        ingredient = Ingredient(ingredient_type, "Test", 1.0)

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.unit
    @pytest.mark.parametrize("name", INGREDIENT_BOUNDARY_NAMES)
    def test_get_name_boundary_value_stores_correctly(self, name):
        """
        Given: граничное значение имени
        When: создаем ингредиент
        Then: имя сохраняется без изменений
        """
        ingredient = Ingredient("sauce", name, 1.0)

        assert ingredient.get_name() == name

    @pytest.mark.unit
    @pytest.mark.parametrize("price", INGREDIENT_BOUNDARY_PRICES)
    def test_get_price_boundary_value_stores_correctly(self, price):
        """
        Given: граничное значение цены
        When: создаем ингредиент
        Then: цена сохраняется без изменений
        """
        ingredient = Ingredient("sauce", "Test", price)

        assert ingredient.get_price() == price

    @pytest.mark.unit
    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_COMBINED_DATA)
    def test_get_type_combined_data_stores_correctly(self, ingredient_type, name, price):
        """
        Given: комбинация граничных/валидных значений
        When: создаем ингредиент
        Then: тип сохраняется корректно
        """
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.unit
    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_COMBINED_DATA)
    def test_get_name_combined_data_stores_correctly(self, ingredient_type, name, price):
        """
        Given: комбинация граничных/валидных значений
        When: создаем ингредиент
        Then: имя сохраняется корректно
        """
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.unit
    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_COMBINED_DATA)
    def test_get_price_combined_data_stores_correctly(self, ingredient_type, name, price):
        """
        Given: комбинация граничных/валидных значений
        When: создаем ингредиент
        Then: цена сохраняется корректно
        """
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price
