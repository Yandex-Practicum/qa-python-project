from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    def test_ingredient_get_price_returns_correct_price(self):
        # Arrange: создаем ингредиент (соус, название, цена)
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Chili", 100)
        
        # Act & Assert: проверяем, что метод get_price() возвращает корректную цену
        assert ingredient.get_price() == 100

    def test_ingredient_get_name_returns_correct_name(self):
        # Arrange: создаем ингредиент (начинка, название, цена)
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Dinosaur cutlet", 200)
        
        # Act & Assert: проверяем, что метод get_name() возвращает корректное имя
        assert ingredient.get_name() == "Dinosaur cutlet"

    def test_ingredient_get_type_returns_correct_type(self):
        # Arrange
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Sour cream", 150)
        
        # Act & Assert: проверяем, что метод get_type() возвращает тип соуса
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
