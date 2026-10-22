from praktikum.database import Database


class TestDatabase:
    """Тесты для класса Database"""

    def test_available_buns(self):
        """Тест: получение доступных булочек"""
        db = Database()
        buns = db.available_buns()
        
        assert isinstance(buns, list)
        assert len(buns) > 0
        # Проверяем, что в базе есть именно те булочки, которые заложены (их должно быть 3)
        assert len(buns) == 3

    def test_available_ingredients(self):
        """Тест: получение доступных ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()
        
        assert isinstance(ingredients, list)
        assert len(ingredients) > 0
        # Проверяем, что в базе есть именно те ингредиенты, которые заложены (их должно быть 6)
        assert len(ingredients) == 6