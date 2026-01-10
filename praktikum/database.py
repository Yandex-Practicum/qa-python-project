from typing import List

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import IngredientTypes


class Database:
    """
    Класс с методами по работе с базой данных.
    """

    def __init__(self):
        self.buns: List[Bun] = []
        self.ingredients: List[Ingredient] = []

        self.buns.append(Bun("black bun", 100))
        self.buns.append(Bun("white bun", 200))
        self.buns.append(Bun("red bun", 300))

        self.ingredients.append(Ingredient(IngredientTypes.INGREDIENT_TYPE_SAUCE, "hot sauce", 100))
        self.ingredients.append(Ingredient(IngredientTypes.INGREDIENT_TYPE_SAUCE, "sour cream", 200))
        self.ingredients.append(Ingredient(IngredientTypes.INGREDIENT_TYPE_SAUCE, "chili sauce", 300))

        self.ingredients.append(Ingredient(IngredientTypes.INGREDIENT_TYPE_FILLING, "cutlet", 100))
        self.ingredients.append(Ingredient(IngredientTypes.INGREDIENT_TYPE_FILLING, "dinosaur", 200))
        self.ingredients.append(Ingredient(IngredientTypes.INGREDIENT_TYPE_FILLING, "sausage", 300))

    def available_buns(self) -> List[Bun]:
        return self.buns

    def available_ingredients(self) -> List[Ingredient]:
        return self.ingredients
