from typing import List

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient

def main():
    # Инициализация базы данных
    database: Database = Database()

    # Создание нового бургера
    burger: Burger = Burger()

    # Получение списка доступных булочек из базы данных
    buns: List[Bun] = database.available_buns()

    # Получение списка доступных ингредиентов из базы данных
    ingredients: List[Ingredient] = database.available_ingredients()

    # Сборка бургера
    if buns:
        burger.set_buns(buns[0])  # Установка булочки

    if len(ingredients) > 5:
        burger.add_ingredient(ingredients[1])  # Добавление ингредиентов
        burger.add_ingredient(ingredients[4])
        burger.add_ingredient(ingredients[3])
        burger.add_ingredient(ingredients[5])

        # Перемещение слоя с ингредиентом
        burger.move_ingredient(2, 1)

        # Удаление ингредиента
        burger.remove_ingredient(3)

    # Печать рецепта бургера
    print(burger.get_receipt())

if __name__ == "__main__":
    main()