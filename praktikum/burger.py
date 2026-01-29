from typing import List
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class Burger:
    """
    Модель бургера.
    Бургер состоит из булочек и ингредиентов (начинка или соус).
    Ингредиенты можно перемещать и удалять.
    Можно распечатать чек с информацией о бургере.
    """

    def __init__(self):
        self.bun = None
        self.ingredients: List[Ingredient] = []

    def set_buns(self, bun: Bun):
        self.bun = bun

    def add_ingredient(self, ingredient: Ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index: int):
        if 0 <= index < len(self.ingredients):
            del self.ingredients[index]

    def move_ingredient(self, index: int, new_index: int):
        if 0 <= index < len(self.ingredients) and 0 <= new_index < len(self.ingredients):
            self.ingredients.insert(new_index, self.ingredients.pop(index))

    def get_price(self) -> float:
        if not self.bun:
            return 0.0  # Без булки бургера нет

        price = self.bun.get_price() * 2
        for ingredient in self.ingredients:
            price += ingredient.get_price()
        return price

    def get_receipt(self) -> str:
        if not self.bun:
            return "Бургер без булки не может существовать!"

        receipt: List[str] = [f'(==== {self.bun.get_name()} ====)']

        for ingredient in self.ingredients:
            receipt.append(f'= {ingredient.get_type().lower()} {ingredient.get_name()} =')

        receipt.append(f'(==== {self.bun.get_name()} ====)\n')
        receipt.append(f'Price: {self.get_price():.2f}')

        return '\n'.join(receipt)

