from typing import List

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient

def main():
    """
    Пример использования классов Bun, Burger, Ingredient и Database для сборки бургера.
    Показывает базовую функциональность программы: добавление, перемещение и удаление ингредиентов,
    а также вывод итогового чека.
    """
    # Инициализируем базу данных и создаём бургер
    database: Database = Database()
    burger: Burger = Burger()

    # Выбираем булку и ингредиенты
    bun: Bun = database.available_buns()[0]
    ingredients: List[Ingredient] = database.available_ingredients()

    # Собираем бургер
    burger.set_buns(bun)
    burger.add_ingredient(ingredients[1])  # Соус: sour cream
    burger.add_ingredient(ingredients[4])  # Начинка: dinosaur
    burger.add_ingredient(ingredients[3])  # Начинка: cutlet
    burger.add_ingredient(ingredients[5])  # Начинка: sausage

    # Меняем порядок ингредиентов и удаляем один
    burger.move_ingredient(2, 1)
    burger.remove_ingredient(3)

    # Выводим чек
    print(burger.get_receipt())

if __name__ == "__main__":
    main()