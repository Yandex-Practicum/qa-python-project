from praktikum.database import Database
from praktikum.burger import Burger


class TestDatabase:
    
    def test_available_buns_returns_list_of_buns(self):
        database = Database()
        buns = database.available_buns()
        assert isinstance(buns, list)
        # Проверяем, что все элементы имеют методы булки
        assert all(hasattr(bun, 'get_name') and hasattr(bun, 'get_price') for bun in buns)

    def test_available_ingredients_returns_list_of_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)
        # Проверяем, что все элементы имеют методы ингредиента
        assert all(hasattr(ing, 'get_name') and hasattr(ing, 'get_price') and hasattr(ing, 'get_type') 
                   for ing in ingredients)

    def test_available_buns_can_be_used_in_burger(self):
        database = Database()
        burger = Burger()
        buns = database.available_buns()
        
        burger.set_buns(buns[0])
        assert burger.bun is not None
        assert burger.bun.get_name() is not None
        assert burger.bun.get_price() >= 0

    def test_available_ingredients_can_be_added_to_burger(self):
        database = Database()
        burger = Burger()
        ingredients = database.available_ingredients()
        
        initial_count = len(burger.ingredients)
        burger.add_ingredient(ingredients[0])
        
        assert len(burger.ingredients) == initial_count + 1
        assert burger.ingredients[0].get_name() is not None
        assert burger.ingredients[0].get_type() is not None

    def test_database_returns_consistent_data(self):
        database = Database()
        buns_first_call = database.available_buns()
        buns_second_call = database.available_buns()
        ingredients_first_call = database.available_ingredients()
        ingredients_second_call = database.available_ingredients()
        
        # Проверяем консистентность возвращаемых данных
        assert len(buns_first_call) == len(buns_second_call)
        assert len(ingredients_first_call) == len(ingredients_second_call)