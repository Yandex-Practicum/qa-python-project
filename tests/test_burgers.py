import pytest
from praktikum.ingredient import Ingredient



class TestBurgers:


    def test_add_first_ingredient(self, burger_with_definite_bun):#Добавление первого ингредиента
        burger_1 = burger_with_definite_bun
        burger_1.add_ingredient(Ingredient('SAUCE', "hot sauce", 100))
        assert burger_1.ingredients[0].name == "hot sauce"


    def test_add_two_ingredient(self, burger_with_definite_bun):#Добавление двух ингредиентов
        burger_1 = burger_with_definite_bun
        burger_1.add_ingredient(Ingredient('SAUCE', "hot sauce", 100))
        burger_1.add_ingredient(Ingredient('SAUCE', "sour cream", 200))
        assert (burger_1.ingredients[0].name == "hot sauce"
                and burger_1.ingredients[1].name == "sour cream"
                )


    def test_add_ingredient(self, burger_with_definite_bun):#Добавление трёх ингредиентов
        burger_1 = burger_with_definite_bun
        burger_1.add_ingredient(Ingredient('SAUCE', "hot sauce", 100))
        burger_1.add_ingredient(Ingredient('SAUCE', "sour cream", 200))
        burger_1.add_ingredient(Ingredient('FILLING', "sausage", 300))
        assert (burger_1.ingredients[0].name == "hot sauce"
                and burger_1.ingredients[1].name == "sour cream"
                and burger_1.ingredients[2].name == "sausage"
                )

    def test_remove_ingredient(self, burger_with_definite_bun):  #Позитивный тест удаление ингредиента
        burger_1 = burger_with_definite_bun
        burger_1.add_ingredient(Ingredient('SAUCE', "hot sauce", 100))
        burger_1.add_ingredient(Ingredient('SAUCE', "sour cream", 200))
        burger_1.add_ingredient(Ingredient('FILLING', "sausage", 300))

        burger_1.remove_ingredient(0)
        assert (burger_1.ingredients[0].type == 'SAUCE'
                and burger_1.ingredients[0].name == "sour cream"
                and burger_1.ingredients[0].price == 200
                and burger_1.ingredients[1].type == 'FILLING'
                and burger_1.ingredients[1].name == "sausage"
                and burger_1.ingredients[1].price == 300
                )


    def test_move_ingredient(self,
                             burger_with_definite_bun):  # Позитивный тест перемещения ингредиента (меняем местами
        # ингредиенты 0 и 2)
        burger_1 = burger_with_definite_bun
        burger_1.add_ingredient(Ingredient('SAUCE', "hot sauce", 100.))
        burger_1.add_ingredient(Ingredient('SAUCE', "sour cream", 200.))
        burger_1.add_ingredient(Ingredient('FILLING', "sausage", 300.))
        burger_1.move_ingredient(2, 0)
        assert (burger_1.ingredients[1].type == 'SAUCE'
                and burger_1.ingredients[1].name == "hot sauce"
                and burger_1.ingredients[1].price == 100.
                and burger_1.ingredients[2].type == 'SAUCE'
                and burger_1.ingredients[2].name == "sour cream"
                and burger_1.ingredients[2].price == 200.
                and burger_1.ingredients[0].type == 'FILLING'
                and burger_1.ingredients[0].name == "sausage"
                and burger_1.ingredients[0].price == 300.
                )

    def test_get_burger_price(self, burger_with_definite_bun):  #Позитивный тест получение стоимости бургера
        burger_1 = burger_with_definite_bun
        burger_1.add_ingredient(Ingredient('SAUCE', "hot sauce", 100.))
        burger_1.add_ingredient(Ingredient('SAUCE', "sour cream", 200.))
        burger_1.add_ingredient(Ingredient('FILLING', "sausage", 300.))
        burger_1.move_ingredient(2, 0)
        actual_price = burger_1.get_price()
        expected_price = (2. * burger_1.bun.price +
                          burger_1.ingredients[0].price + burger_1.ingredients[1].price +
                          burger_1.ingredients[2].price)
        assert actual_price == expected_price

    def test_get_receipt(self, burger_with_definite_bun):#Позитивный тест получения чека
        burger_1 = burger_with_definite_bun
        burger_1.add_ingredient(Ingredient('SAUCE', "hot sauce", 100.))
        burger_1.add_ingredient(Ingredient('SAUCE', "sour cream", 200.))
        burger_1.add_ingredient(Ingredient('FILLING', "sausage", 300.))
        receipt_actual = burger_1.get_receipt()
        receipt_expected = ('(==== black bun ====)' +
                            '\n' +'= sauce hot sauce =' +
                            '\n' + '= sauce sour cream =' +
                            '\n' + '= filling sausage =' +
                            '\n' + '(==== black bun ====)' +
                            '\n' + '\n' + 'Price: 800.0')
        assert receipt_actual == receipt_expected
