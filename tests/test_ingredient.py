import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:
    @pytest.mark.parametrize("name, price, ingredient_type", [
        ("Соус Spicy-X", 90, "SAUCE"),
        ("Соус фирменный Space Sauce", 80, "SAUCE"),
        ("Соус традиционный галактический", 15, "SAUCE"),
        ("Соус с шипами Антарианского плоскоходца", 88, "SAUCE"),
        ("Мясо бессмертных моллюсков Protostomia", 1337, "FILLING"),
        ("Говяжий метеорит (отбивная)", 3000, "FILLING"),
        ("Биокотлета из марсианской Магнолии", 424, "FILLING"),
        ("Филе Люминесцентного тетраодонтимформа", 988, "FILLING"),
        ("Хрустящие минеральные кольца", 300, "FILLING"),
        ("Плоды Фалленианского дерева", 874, "FILLING"),
        ("Кристаллы марсианских альфа-сахаридов", 762, "FILLING"),
        ("Мини-салат Экзо-Плантаго", 4400, "FILLING"),
        ("Сыр с астероидной плесенью", 4142, "FILLING")
    ])
    def test_ingredient_getters(self, name, price, ingredient_type):
        # Создаем объект ингредиента с типом
        ingred = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        # Проверка получения имени, цены и типа ингредиента
        assert ingred.get_name() == name
        assert ingred.get_price() == price
        assert ingred.get_type() == ingredient_type

    def test_ingredient_invalid_name(self):
        # Проверка на пустое название
        with pytest.raises(ValueError):
            Ingredient(ingredient_type="SAUCE", name="", price=50)

    def test_ingredient_invalid_price(self):
        # Проверка на отрицательную цену
        with pytest.raises(ValueError):
            Ingredient(ingredient_type="SAUCE", name="Салат", price=-5)
