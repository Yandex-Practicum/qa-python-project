import pytest
from Diplom_1.burger import Burger
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:

    @pytest.fixture
    def burger(self):
        """
        Фикстура для создания пустого бургера.
        """
        return Burger()

    @pytest.fixture
    def bun(self):
        """
        Фикстура для создания булочки.
        """
        return Bun("black bun", 100)

    @pytest.fixture
    def sauce(self):
        """
        Фикстура для создания соуса.
        """
        return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

    @pytest.fixture
    def filling(self):
        """
        Фикстура для создания начинки.
        """
        return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)

    def test_set_buns(self, burger, bun):
        """
        Проверяет установку булочки в бургер.
        """
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, burger, sauce, filling):
        """
        Проверяет добавление ингредиентов в бургер.
        """
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == sauce
        assert burger.ingredients[1] == filling

    def test_remove_ingredient(self, burger, sauce, filling):
        """
        Проверяет удаление ингредиента из бургера.
        """
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == filling

    def test_move_ingredient(self, burger, sauce, filling):
        """
        Проверяет перемещение ингредиента в бургере.
        """
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == filling
        assert burger.ingredients[1] == sauce

    @pytest.mark.parametrize(
        "bun_price, sauce_price, filling_price, expected_price",
        [
            (100.0, 200.0, 300.0, 700.0),  # Стандартные цены
            (200.5, 100.3, 100.4, 601.7),  # Измененные цены
            (0.0, 0.0, 0.0, 0.0),  # Бесплатный бургер
        ],
    )
    def test_get_price(self, burger, bun, sauce, filling, bun_price, sauce_price, filling_price, expected_price):
        """
        Проверяет расчет стоимости бургера с использованием параметризации.
        """
        # Переопределяем цены булочки и ингредиентов
        bun.price = bun_price
        sauce.price = sauce_price
        filling.price = filling_price

        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize(
        "bun_name, sauce_name, filling_name",
        [
            ("black bun", "hot sause", "coutlet"),
            ("black bun", "sour cream", "dinosaur"),
            ("black bun", "chili sause", "sausage"),
            ("white bun", "sour cream", "sausage"),
            ("white bun", "chili sause","coutlet"),
            ("white bun", "hot sause", "dinosaur"),
            ("red bun", "chili sause", "dinosaur"),
            ("red bun", "hot sause", "sausage"),
            ("red bun", "sour cream", "coutlet")
        ],
    )

        def test_get_receipt(self, burger, bun, sauce, filling, bun_name, sauce_name, filling_name):
        """
        Проверяет формирование рецепта для бургера.
        """
        bun.price = bun_name
        sauce.price = sauce_name
        filling.price = filling_name

        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        receipt = burger.get_receipt()
        # формируем контрольный рецепт с теми же ингредиентами
        receipt_control = "Price: "+str(bun_name)+str(bun_name)+str(sauce_name)+str(filling_name)

        assert isinstance(receipt, str)
        #Проверяем, что в рецепте есть ожидаемые элементы (можно разбить на несколько assert)
        assert f'(==== {bun.get_name()} ====)' in receipt
        assert f'= {INGREDIENT_TYPE_SAUCE.lower()} {sauce.get_name()} =' in receipt
        assert f'= {INGREDIENT_TYPE_FILLING.lower()} {filling.get_name()} =' in receipt
        assert f'Price: {burger.get_price()}' in receipt
        assert f'Price: {burger.get_price()}' == receipt_control, "Рецептура неверная"
