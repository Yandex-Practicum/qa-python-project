from typing import List
from bun import Bun
from ingredient import Ingredient


class Burger:
   
    #Модель бургера.
    #Бургер состоит из булочек и ингредиентов (начинка или соус).
    #Ингредиенты можно перемещать и удалять.
    #Можно распечать чек с информацией о бургере.

    def __init__(self):
        self.bun = None
        self.ingredients: List[Ingredient] = []

    def set_buns(self, bun: Bun):
        """Установить булку для бургера"""
        self.bun = bun

    def add_ingredient(self, ingredient: Ingredient):
        """Добавить ингредиент в бургер"""
        self.ingredients.append(ingredient)

    def remove_ingredient(self, index: int):
        """Удалить ингредиент по индексу с проверкой"""
        if index < 0 or index >= len(self.ingredients):
            raise IndexError("Invalid ingredient index")
        del self.ingredients[index]

    def move_ingredient(self, index: int, new_index: int):
        """Переместить ингредиент на новый индекс с проверкой"""
        if index < 0 or index >= len(self.ingredients) or new_index < 0 or new_index >= len(self.ingredients):
            raise IndexError("Invalid ingredient index")
        self.ingredients.insert(new_index, self.ingredients.pop(index))

    def get_price(self) -> float:
        """Вернуть цену бургера, учитывая булку и ингредиенты"""
        price = 0
        if self.bun is not None:
            price += self.bun.get_price() * 2
        for ingredient in self.ingredients:
            price += ingredient.get_price()
        return price

    def get_receipt(self) -> str:
        """Вернуть чек бургера в виде строки"""
        receipt: List[str] = []

        if self.bun is not None:
            receipt.append(f'(==== {self.bun.get_name()} ====)')

        for ingredient in self.ingredients:
            receipt.append(f'= {ingredient.get_type().lower()} {ingredient.get_name()} =')

        if self.bun is not None:
            receipt.append(f'(==== {self.bun.get_name()} ====)\n')
        else:
            # Добавляем пустую строку перед ценой, чтобы соответствовать тесту
            receipt.append("")

        receipt.append(f'Price: {self.get_price()}')
        return '\n'.join(receipt)
