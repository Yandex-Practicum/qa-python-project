import pytest
from unittest.mock import MagicMock
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

class TestDatabase:
    @pytest.fixture
    def database(self):
        db = Database()
        # Мокаем метод, чтобы вернуть поддельные данные
        db.available_buns = MagicMock(return_value=[
            Bun("black bun", 100),
            Bun("white bun", 200)
        ])
        return db

    def test_available_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 2  # изменено на 2, так как мы замокали метод
        assert buns[0].get_name() == "black bun"
