from typing import List
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


def main():
    # Инициализируем базу данных
    database: Database = Database()

    # Создадим новый бургер
    burger: Burger = Burger()

    # Получаем булки и ингредиенты из базы данных
    buns: List[Bun] = database.available_buns()
    ingredients: List[Ingredient] = database.available_ingredients()

    # Собираем бургер
    if buns:
        burger.set_buns(buns[0])

    if len(ingredients) >= 4:
        burger.add_ingredient(ingredients[1])
        burger.add_ingredient(ingredients[4])
        burger.add_ingredient(ingredients[3])
        burger.add_ingredient(ingredients[5])

        # Перемещаем ингредиент
        burger.move_ingredient(2, 1)

        # Удаляем ингредиент
        burger.remove_ingredient(3)

    # Распечатываем рецепт бургера
    print(burger.get_receipt())


if __name__ == "__main__":
    main()

