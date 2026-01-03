import pytest
import allure

from praktikum.database import Database


class TestDatabase:


    # Ннууу... могу проверить, что экземпляр создается, а в нем создаются списки и заполняются данными: непустое И (в наличии и непустое) И (в наличии и непустое)

    @allure.title('Тестирование создания экземпляря Database')
    @allure.description('Проверка, что есть экземпляр, у него есть непустой список buns и непустой список ingredients')
    def test_init (self):
        db = Database()
        assert db and db.buns and db.ingredients


#  Предвижу комментарий: "Создание экземпляра Database должно быть в фикстуре"
#  И сразу говорю, что специально не выносила: создание  - одно выражение. Создавать фикстуру, а потом прописвать ее в каждом методе по объему больше плюс добавляются запуски фикстур, передача данных итд.

    @allure.title('Тестирование метода available_buns()')
    @allure.description('Сравнение результатов работы метода и переменной buns')
    def test_available_bun (self):
        db = Database()
        assert (db.available_buns()==db.buns)



    @allure.title('Тестирование метода available_ingredients()')
    @allure.description('Сравнение результатов работы метода и переменной ingredients')
    def test_available_ingredient (self):
        db = Database()
        assert (db.available_ingredients() == db.ingredients)