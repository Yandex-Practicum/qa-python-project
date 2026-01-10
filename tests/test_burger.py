from Diplom_1.practikum.bun import Bun
from Diplom_1.practikum.ingredient import Ingredient
from Diplom_1.practikum.burger import Burger

class TestBurgerMethods:
    def test_set_buns(self):
        self.burger = Burger()
        bun = Bun('Грязнуля', 2.40)
        self.burger.set_buns(bun)
        assert self.burger.bun.get_name() == "Грязнуля"

    def test_add_ingredient(self):
        self.burger = Burger()
        ingredient = Ingredient('Овощи', 'помидор', 2.20)  # Initialize Ingredient with name and price
        self.burger.add_ingredient(ingredient)
        assert len(self.burger.ingredients) == 1

    def test_remove_ingredient(self):
        self.burger = Burger()
        self.burger.add_ingredient(Ingredient('Овощи', 'помидор', 2.20))
        self.burger.add_ingredient(Ingredient('Овощи', 'салат', 2.20))
        self.burger.remove_ingredient(0)
        assert len(self.burger.ingredients) == 1

    def test_move_ingredient(self):
        self.burger = Burger()
        ingredient1 = Ingredient('Овощи', 'Лук', 2.20)
        ingredient2 = Ingredient('Овощи', 'Сыр', 2.25)
        self.burger.add_ingredient(ingredient1)
        self.burger.add_ingredient(ingredient2)
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[1].get_name() == 'Лук'

    def test_get_price(self):
        self.burger = Burger()
        bun = Bun('Неряха Джо', 3.25)
        self.burger.set_buns(bun)
        ingredient1 = Ingredient('Основа', 'Котлета', 2.00)
        ingredient2 = Ingredient('Овощи','Салат', 0.75)
        self.burger.add_ingredient(ingredient1)
        self.burger.add_ingredient(ingredient2)
        assert self.burger.get_price() == 9.25

    def test_get_receipt(self):
        bun = Bun('Неряха Джо', 3.25)
        ingredient1 = Ingredient('Овощи', 'Лук', 2.20)
        ingredient2 = Ingredient('Овощи', 'Салат', 0.75)
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        assert 'Неряха Джо' in burger.get_receipt()
