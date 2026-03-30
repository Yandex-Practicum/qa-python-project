# burger.py

# Мы сами определяем классы Bun и Ingredient, так как их нет во внешней библиотеке.
class Bun:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

class Ingredient:
    def __init__(self, ingredient_type: str, name: str, price: float):
        self.type = ingredient_type
        self.name = name
        self.price = price

    def get_type(self) -> str:
        return self.type

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

# --- Код класса Burger ---
from typing import List, Optional

class Burger:
    def __init__(self):
        self.bun: Optional[Bun] = None
        self.ingredients: List[Ingredient] = []

    def set_buns(self, bun: Bun) -> None:
        self.bun = bun

    def add_ingredient(self, ingredient: Ingredient) -> None:
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index: int) -> None:
        if 0 <= index < len(self.ingredients):
            self.ingredients.pop(index)

    def move_ingredient(self, from_index: int, to_index: int) -> None:
        if 0 <= from_index < len(self.ingredients) and 0 <= to_index < len(self.ingredients):
            ingredient = self.ingredients.pop(from_index)
            self.ingredients.insert(to_index, ingredient)

    def get_price(self) -> float:
        if not self.bun:
            return 0.0

        buns_price = self.bun.get_price() * 2
        ingredients_price = sum(ing.get_price() for ing in self.ingredients)
        return buns_price + ingredients_price

    def get_receipt(self) -> str:
        if not self.bun:
            return ""

        receipt = f"(==== {self.bun.get_name()} ====)\n"
        for ingredient in self.ingredients:
            receipt += f"= {ingredient.get_type().lower()} {ingredient.get_name()} =\n"
        receipt += f"(==== {self.bun.get_name()} ====)\n"
        receipt += f"\nPrice: {self.get_price()}"
        return receipt
