import sys
import os

# добавить директорию в path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from praktikum.database import Database


class TestDatabase:
    
    #Тест на проверку кол-ва записей по булкам
    def test_create_database_available_buns_amt_is_correct(self) -> None:
        database = Database()
        assert len(database.available_buns()) == 3
        
    #Тест на проверку кол-ва записей по ингридиентам
    def test_create_database_available_ingredients_amt_is_correct(self) -> None:
        database = Database()
        assert len(database.available_ingredients()) == 6