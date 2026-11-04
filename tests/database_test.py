from praktikum.database import Database

class TestDatabase:

    def test_database_available_buns_returns_correct_count(self):
        # Arrange: инициализируем базу данных
        db = Database()
        
        # Act: получаем список доступных булочек
        buns = db.available_buns()
        
        # Assert: проверяем, что в базе ровно 3 вида булочек
        assert len(buns) == 3

    def test_database_available_ingredients_returns_correct_count(self):
        # Arrange
        db = Database()
        
        # Act: получаем список доступных ингредиентов
        ingredients = db.available_ingredients()
        
        # Assert: проверяем, что в базе ровно 6 ингредиентов
        assert len(ingredients) == 6

    def test_database_buns_have_correct_data(self):
        # Arrange
        db = Database()
        
        # Act
        buns = db.available_buns()
        
        # Assert: проверяем имя первой булочки в списке
        assert buns[0].get_name() == "black bun"
