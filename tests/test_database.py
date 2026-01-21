from praktikum.database import Database


class TestDatabase:
    """
    Тесты для класса Database, который предоставляет данные о булочках и ингредиентах.
    """

    def test_count_available_buns(self) -> None:
        """
        Проверяет, что метод available_buns() возвращает правильное количество булочек.
        """
        database = Database()
        buns = database.available_buns()
        expected_count = 3

        assert len(buns) == expected_count, f"Ожидалось {expected_count} булочек, но найдено {len(buns)}"

        # Дополнительная проверка на структуру булочек
        for bun in buns:
            assert hasattr(bun, 'get_name'), "У булочки отсутствует метод get_name()"
            assert hasattr(bun, 'get_price'), "У булочки отсутствует метод get_price()"

    def test_count_available_ingredients(self) -> None:
        """
        Проверяет, что метод available_ingredients() возвращает правильное количество ингредиентов.
        """
        database = Database()
        ingredients = database.available_ingredients()
        expected_count = 6

        assert len(ingredients) == expected_count, f"Ожидалось {expected_count} ингредиентов, но найдено {len(ingredients)}"

        # Дополнительная проверка на структуру ингредиентов
        for ingredient in ingredients:
            assert hasattr(ingredient, 'get_name'), "У ингредиента отсутствует метод get_name()"
            assert hasattr(ingredient, 'get_price'), "У ингредиента отсутствует метод get_price()"
            assert hasattr(ingredient, 'get_type'), "У ингредиента отсутствует метод get_type()"

    def test_available_buns_non_empty(self) -> None:
        """
        Проверяет, что список доступных булочек не пустой.
        """
        database = Database()
        buns = database.available_buns()

        assert buns, "Список доступных булочек пустой, ожидаются данные"

    def test_available_ingredients_non_empty(self) -> None:
        """
        Проверяет, что список доступных ингредиентов не пустой.
        """
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients, "Список доступных ингредиентов пустой, ожидаются данные"
