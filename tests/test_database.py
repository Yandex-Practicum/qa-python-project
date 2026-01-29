import pytest

class TestDataBase:
    def test_count_buns(self, data_base):
        assert len(data_base.buns) == 3


    def test_count_ingredients(self, data_base):
        assert len(data_base.ingredients) == 6


    @pytest.mark.parametrize('index, bun_name, bun_price',
                             [
                                 (0, 'black bun', 100),
                                 (1, 'white bun', 200),
                                 (2, 'red bun', 300)
                             ])
    def test_data_base_buns(self, data_base, index, bun_name, bun_price):
        bun = data_base.buns[index]
        assert bun.name == bun_name and bun.price == bun_price

    @pytest.mark.parametrize('index, ingredient_type, ingredient_name, ingredient_price',
                            [
                                (0, 'SAUCE', 'hot sauce', 100),
                                (1, 'SAUCE', 'sour cream', 200),
                                (2, 'SAUCE', 'chili sauce', 300),
                                (3, 'FILLING', 'cutlet', 100),
                                (4, 'FILLING', 'dinosaur', 200),
                                (5, 'FILLING', 'sausage', 300)
                            ])
    def test_data_base_ingredients(self, data_base, index, ingredient_type, ingredient_name, ingredient_price):
        ingredient = data_base.ingredients[index]
        assert ingredient.type == ingredient_type
        assert ingredient.name == ingredient_name
        assert ingredient.price == ingredient_price


    def test_available_buns_success(self, data_base):
        buns = data_base.available_buns()
        assert len(buns) == 3
        assert buns[0].name == "black bun" and buns[0].price == 100
        assert buns[1].name == "white bun" and buns[1].price == 200
        assert buns[2].name == "red bun" and buns[2].price == 300


    def test_available_ingredients_success(self, data_base):
        ingredients = data_base.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[0].type == "SAUCE" and ingredients[0].name == "hot sauce" and ingredients[0].price == 100
        assert ingredients[1].type == "SAUCE" and ingredients[1].name == "sour cream" and ingredients[1].price == 200
        assert ingredients[2].type == "SAUCE" and ingredients[2].name == "chili sauce" and ingredients[2].price == 300
        assert ingredients[3].type == "FILLING" and ingredients[3].name == "cutlet" and ingredients[0].price == 100
        assert ingredients[4].type == "FILLING" and ingredients[4].name == "dinosaur" and ingredients[1].price == 200
        assert ingredients[5].type == "FILLING" and ingredients[5].name == "sausage" and ingredients[2].price == 300