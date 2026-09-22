import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock


class TestBurger:

    @pytest.mark.parametrize('name', ['Флюоресцентная булочка R2-D2', 'Краторная булка N-200i'])
    def test_set_buns_success(self, burger, mock_bun, name):
        mock_bun.get_name.return_value = name
        burger.set_buns(mock_bun)
        assert burger.bun is mock_bun
    
    @pytest.mark.parametrize('old_name,new_name', [('Флюоресцентная булочка R2-D2', 'Краторная булка N-200i'), ('Краторная булка N-200i', 'Флюоресцентная булочка R2-D2')])
    def test_set_buns_replaces_correctly_existing_bun(self, burger, old_name, new_name):
        old_bun = Mock()
        old_bun.get_name.return_value = old_name
        old_bun.get_price.return_value = 988.0
        burger.set_buns(old_bun)
        new_bun = Mock()
        new_bun.get_name.return_value = new_name
        new_bun.get_price.return_value = 988.0
        burger.set_buns(new_bun)
        assert burger.bun is new_bun
    
    @pytest.mark.parametrize('wrong_value', ['bread', 123, ['булочка'], {'name':'булочка'}, None])
    def test_set_buns_accepts_any_object_without_raising_error(self, burger, wrong_value):
        burger.set_buns(wrong_value)
        assert burger.bun == wrong_value

    @pytest.mark.parametrize('ingredient_type,name', [
                (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X'),
                (INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce'),
                (INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический'),
                (INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца'),
                (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia'),
                (INGREDIENT_TYPE_FILLING, 'Говяжий метеорит (отбивная)'),
                (INGREDIENT_TYPE_FILLING, 'Биокотлета из марсианской Магнолии'),
                (INGREDIENT_TYPE_FILLING, 'Филе Люминесцентного тетраодонтимформа'),
                (INGREDIENT_TYPE_FILLING, 'Хрустящие минеральные кольца'),
                (INGREDIENT_TYPE_FILLING, 'Плоды Фалленианского дерев'),
                (INGREDIENT_TYPE_FILLING, 'Кристаллы марсианских альфа-сахаридов'),
                (INGREDIENT_TYPE_FILLING, 'Мини-салат Экзо-Плантаго'),
                (INGREDIENT_TYPE_FILLING, 'Сыр с астероидной плесенью')])
    def test_add_ingredients_add_one_item_success(self, burger, ingredient_type, name):
        mock_ingr = Mock()
        mock_ingr.get_type.return_value = ingredient_type
        mock_ingr.get_name.return_value = name
        mock_ingr.get_price.return_value = 0.0
        burger.add_ingredient(mock_ingr)
        assert burger.ingredients[-1] is mock_ingr    
        
    def test_add_ingredient_add_mupltiple_items_in_order_success(self, burger):
        ingr_1 = Mock()
        ingr_1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingr_1.get_name.return_value = 'Соус Spicy-X'
        ingr_1.get_price.return_value = 0.0
        ingr_2 = Mock()
        ingr_2.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingr_2.get_name.return_value = 'Филе Люминесцентного тетраодонтимформа'
        ingr_2.get_price.return_value = 0.0
        ingr_3 = Mock()
        ingr_3.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingr_3.get_name.return_value = 'Мини-салат Экзо-Плантаго'
        ingr_3.get_price.return_value = 0.0
       
        burger.add_ingredient(ingr_1) 
        burger.add_ingredient(ingr_2)  
        burger.add_ingredient(ingr_3)    
        assert burger.ingredients == [ingr_1, ingr_2, ingr_3]                  
        
    def test_add_ingredient_add_duplicate_success(self, burger):
        ingr = Mock()
        ingr.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingr.get_name. return_value = 'Соус Spicy-X'
        ingr.get_price.return_value = 0.0 
        burger.add_ingredient(ingr) 
        burger.add_ingredient(ingr) 
        assert burger.ingredients == [ingr, ingr]
        
    def test_add_ingredient_list_is_initially_empty(self, burger):
        ingr = Mock()
        ingr.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingr.get_name. return_value = 'Соус Spicy-X'
        ingr.get_price.return_value = 0.0 
        burger.add_ingredient(ingr)
        assert len(burger.ingredients) == 1
        
    @pytest.mark.parametrize('wrong_value', ['сыр', 123, ['ингредиент'], {'name':'соус'}, None])
    def test_add_ingredient_accept_any_value(self, burger, wrong_value):
        burger.add_ingredient(wrong_value)
        assert wrong_value in burger.ingredients

    def test_remove_ingredient_by_index_success(self, burger_with_ingredients):
            burger = burger_with_ingredients
            burger.remove_ingredient(1)
            assert len(burger.ingredients) == 2
    
    def test_remove_ingredient_only_item_leaves_empty_list(self, burger):
        ingr = Mock()
        ingr.name = "Говяжий метеорит (отбивная)"
        ingr.get_price.return_value = 0.0
        ingr.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(ingr)
        burger.remove_ingredient(0)
        assert burger.ingredients == []
    
    def test_remove_ingredient_negative_index_works(self, burger_with_ingredients):
        burger = burger_with_ingredients
        burger.remove_ingredient(-1)  
        assert len(burger.ingredients) == 2
    
    def test_remove_first_ingredient_success(self, burger_with_ingredients):
        burger = burger_with_ingredients
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 2
    
    def test_remove_first_ingredient_content_check(self, burger_with_ingredients):
        burger = burger_with_ingredients
        burger.remove_ingredient(0)
        assert burger.ingredients[0].name == 'Соус с шипами Антарианского плоскоходца'
    
    def test_remove_last_ingredient_success(self, burger_with_ingredients):
        burger = burger_with_ingredients
        burger.remove_ingredient(2)
        assert len(burger.ingredients) == 2
    
    def test_remove_last_ingredient_content_check(self, burger_with_ingredients):
        burger = burger_with_ingredients
        burger.remove_ingredient(2)
        assert burger.ingredients[-1].name == 'Соус с шипами Антарианского плоскоходца'
    
    def test_remove_ingredient_invalid_index_error(self, burger_with_ingredients):
        burger = burger_with_ingredients
        initial_len = len(burger.ingredients)
        with pytest.raises(IndexError):
            burger.remove_ingredient(6)
        assert len(burger.ingredients) == initial_len
    
    def test_remove_ingredient_from_empty_list_error(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient_forward_by_one(self, burger_with_ingredients):
        burger = burger_with_ingredients
        burger.move_ingredient(1, 0)  
        assert burger.ingredients[0].name == 'Соус с шипами Антарианского плоскоходца'
    
    def test_move_ingredient_backward_through_one(self, burger_with_ingredients):
        burger = burger_with_ingredients
        burger.move_ingredient(0, 2)  
        assert burger.ingredients[2].name == 'Соус традиционный галактический'
    
    def test_move_ingredient_same_position_no_change(self, burger_with_ingredients):
        burger = burger_with_ingredients
        no_change_list = burger.ingredients.copy()
        burger.move_ingredient(1, 1)
        assert burger.ingredients == no_change_list
    
    def test_move_ingredient_preserves_list_length(self, burger_with_ingredients):
        burger = burger_with_ingredients
        initial_len = len(burger.ingredients)
        burger.move_ingredient(0, 2) 
        assert len(burger.ingredients) == initial_len
    
    def test_move_ingredient_with_negative_index(self, burger_with_ingredients):
        burger = burger_with_ingredients
        burger.move_ingredient(-1, 0)
        assert burger.ingredients[0].name == 'Мясо бессмертных моллюсков Protostomia'
    
    def test_move_ingredient_raises_index_error_on_invalid_index(self, burger_with_ingredients):
        burger = burger_with_ingredients
        initial_list = burger.ingredients.copy()
        with pytest.raises(IndexError):
            burger.move_ingredient(5, 0)
        assert burger.ingredients == initial_list


    def test_get_price_correct_calculation(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected = (2 * mock_bun.get_price.return_value) + mock_sauce.get_price.return_value + mock_filling.get_price.return_value
        assert burger.get_price() == expected

    def test_get_price_only_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)    
        expected = 2 * mock_bun.get_price.return_value
        assert burger.get_price() == expected

    def test_get_price_multiple_ingredient(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_sauce)
        expected = (2 * mock_bun.get_price.return_value) + (2 * mock_sauce.get_price.return_value)
        assert burger.get_price() == expected

    def test_get_price_after_racing_buns(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        first_price = burger.get_price()
        new_bun = Mock()
        new_bun.name.return_value = 'New Bun'
        new_bun.get_price.return_value = 1255.0
        burger.set_buns(new_bun)
        new_price = burger.get_price()
        assert new_price != first_price

    def test_get_price_without_bun_error(self, burger):
        with pytest.raises(AttributeError):
            burger.get_price()
        assert not hasattr(burger, "bun") or burger.bun is None

    def test_get_receipt_success(self, burger, mock_bun, mock_filling, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        receipt = burger.get_receipt()
        expected_price = burger.get_price()
        expected_lines = [
            "(==== Test Bun ====)",
            "= sauce Spicy-X =",
            "= filling Protostomia =",
            "(==== Test Bun ====)",
            "",
            f"Price: {expected_price}",
            ]
        expected_receipt = "\n".join(expected_lines)
        assert receipt == expected_receipt

    def test_get_receipt_no_ingredient(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        expected_price = 2 * mock_bun.get_price.return_value
        expected_lines = [
                    "(==== Test Bun ====)",
                    "(==== Test Bun ====)",
                    "",
                    f"Price: {expected_price}",
                    ]
        expected_receipt = "\n".join(expected_lines)
        assert receipt == expected_receipt

    def test_get_receipt_ingredient_type_lowercase(self, burger, mock_bun, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        receipt = burger.get_receipt()
        assert "= filling Protostomia =" in receipt

    def test_get_receipt_top_and_bottom_buns_are_identical(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        result = burger.get_receipt()
        lines = result.split('\n')
        assert lines[0] == lines[1] 

    def test_get_receipt_top_bun_frame(self, burger, mock_bun, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        result = burger.get_receipt()
        assert "(==== Test Bun ====" in result

    def test_receipt_ingredient_line_format(self, burger, mock_bun, mock_sauce, mock_filling): 
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        burger.add_ingredient(mock_sauce)
        result = burger.get_receipt()
        assert ("= filling Protostomia =" in result) and ("= sauce Spicy-X =" in result)

    def test_get_receipt_bottom_bun_frame(self, burger, mock_bun, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        result = burger.get_receipt()
        assert "(==== Test Bun ====" in result.split('\n')[-3]

    def test_get_receipt_price_last_line(self, burger, mock_bun, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_filling)
        result = burger.get_receipt()
        expected_price = 2 * mock_bun.get_price.return_value + mock_filling.get_price.return_value
        assert result.endswith(f"Price: {expected_price}")

    def test_get_receipt_structure_with_empty_ingredient_name(self, burger, mock_bun, mock_ingredient_empty_name):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_empty_name)
        result = burger.get_receipt()
        assert "= filling  =" in result

    def test_get_receipt_displays_negative_price_correctly(self, burger, mock_bun, mock_ingredient_negative_price):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_negative_price)
        result = burger.get_receipt()
        assert "Price: 1966.0" in result

    def test_get_receipt_no_bun_error(self, burger):
        with pytest.raises(AttributeError): 
            burger.get_receipt()
        assert not hasattr(burger, "bun") or burger.bun is None