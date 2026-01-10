from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from typing import List
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class DatabaseMock(Database):
    """
    Поддельный класс для тестирования других классов с использованием базы данных.
    """

    def __init__(self):
        super().__init__()

    def available_buns(self) -> List[Bun]:
        return [Bun("mock bun 1", 400),
                Bun("mock bun 2", 500)]  # Возвращаем заранее заданные "мок" булочки для тестирования

    def available_ingredients(self) -> List[Ingredient]:
        return [Ingredient(INGREDIENT_TYPE_SAUCE, "mock sauce 1", 400),
                Ingredient(INGREDIENT_TYPE_FILLING, "mock filling 1",
                           500)]  # Возвращаем заранее заданные "мок" ингредиенты для тестирования
