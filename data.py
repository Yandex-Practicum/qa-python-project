from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestData:
    ingredients = [
        ["Начинки", "Биокотлета из марсианской Магнолии", 424],
        ["Начинки", "Филе Люминесцентного тетраодонтимформа", 988],
        ["Начинки", "Мясо бессмертных моллюсков", 1337],
        ["Начинки", "Говяжий метеорит (отбивная)", 3000],
        ["Начинки", "Хрустящие минеральные кольца", 300],
        ["Начинки", "Плоды Фалленианского дерева", 874],
        ["Начинки", "Кристаллы марсианских альфа-сахаридов", 762],
        ["Начинки", "Мини-салат Экзо-Плантаго", 4400],
        ["Начинки", "Сыр с астероидной плесенью", 4142],
        ["Соусы", "Соус Spicy-X", 90],
        ["Соусы", "Соус фирменный Space Sauce", 80],
        ["Соусы", "Соус традиционный галактический", 15],
        ["Соусы", "Соус с шипами Антарианского плоскоходца", 88],
    ]
    buns = [["Ржаная булочка", 100], ["Безглютеновая булка", 9999]]
    expected_buns = {"black bun": 100, "white bun": 200, "red bun": 300}
    expected_ingredients = {
        "hot sauce": (INGREDIENT_TYPE_SAUCE, 100),
        "sour cream": (INGREDIENT_TYPE_SAUCE, 200),
        "chili sauce": (INGREDIENT_TYPE_SAUCE, 300),
        "cutlet": (INGREDIENT_TYPE_FILLING, 100),
        "dinosaur": (INGREDIENT_TYPE_FILLING, 200),
        "sausage": (INGREDIENT_TYPE_FILLING, 300),
    }
