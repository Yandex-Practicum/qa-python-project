# test_database.py
import pytest
import allure
from database import Database


class TestDatabase:

    @allure.title('Проверяем доступно 3 булочки')
    def test_available_buns_count(self):
        db = Database()
        buns = db.available_buns()
        allure.attach(
            name="Список булочек",
            body="\n".join(f"{b.get_name()} — {b.get_price()}" for b in buns),
            attachment_type=allure.attachment_type.TEXT
        )
        assert len(buns) == 3, "Должно быть 3 булочки"

    @allure.title('Проверяем имя булочки: {param_id}')
    @pytest.mark.parametrize(
        'index, expected_name',
        [
            (0, "black bun"),
            (1, "white bun"),
            (2, "red bun"),
        ],
        ids=[
            "1я - black bun",
            "2я - white bun",
            "3я - red bun"
        ]
    )
    def test_available_buns_names(self, index, expected_name):
        db = Database()
        buns = db.available_buns()
        allure.attach(
            name="Список булочек",
            body="\n".join(f"{b.get_name()} — {b.get_price()}" for b in buns),
            attachment_type=allure.attachment_type.TEXT
        )
        assert buns[index].get_name() == expected_name, f"Булочка {index} должна называться {expected_name}"

    @allure.title('Проверяем цену булочки: {param_id}')
    @pytest.mark.parametrize(
        'index, expected_price',
        [
            (0, 100),
            (1, 200),
            (2, 300),
        ],
        ids=[
            "1я - black bun — 100 руб.",
            "2я - white bun — 200 руб.",
            "3я - red bun — 300 руб."
        ]
    )
    def test_available_buns_prices(self, index, expected_price):
        db = Database()
        buns = db.available_buns()
        allure.attach(
            name="Список булочек",
            body="\n".join(f"{b.get_name()} — {b.get_price()}" for b in buns),
            attachment_type=allure.attachment_type.TEXT
        )
        assert buns[index].get_price() == expected_price, f"Цена булочки {index} должна быть {expected_price}"

    @allure.title('Проверяем доступно 6 ингредиентов')
    def test_available_ingredients_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        allure.attach(
            name="Список ингредиентов",
            body="\n".join(f"{i.get_type()} - {i.get_name()} — {i.get_price()}" for i in ingredients),
            attachment_type=allure.attachment_type.TEXT
        )
        assert len(ingredients) == 6, "Должно быть 6 ингредиентов"

    @allure.title('Проверяем тип ингредиента: {param_id}')
    @pytest.mark.parametrize(
        'index, expected_type',
        [
            (0, "SAUCE"),
            (3, "FILLING"),
        ],
        ids=[
            "1й - SAUCE (соус)",
            "4й - FILLING (начинка)"
        ]
    )
    def test_ingredient_types(self, index, expected_type):
        db = Database()
        ingredients = db.available_ingredients()
        allure.attach(
            name="Список ингредиентов",
            body="\n".join(f"{i.get_type()} - {i.get_name()} — {i.get_price()}" for i in ingredients),
            attachment_type=allure.attachment_type.TEXT
        )
        assert ingredients[index].get_type() == expected_type, f"Ингредиент {index} должен быть тип {expected_type}"

    @allure.title('Проверяем название ингредиента: {param_id}')
    @pytest.mark.parametrize(
        'index, expected_name',
        [
            (0, "hot sauce"),
            (1, "sour cream"),
            (2, "chili sauce"),
            (3, "cutlet"),
            (4, "dinosaur"),
            (5, "sausage"),
        ],
        ids=[
            "1й - hot sauce",
            "2й - sour cream",
            "3й - chili sauce",
            "4й - cutlet",
            "5й - dinosaur",
            "6й - sausage"
        ]
    )
    def test_ingredient_names(self, index, expected_name):
        db = Database()
        ingredients = db.available_ingredients()
        allure.attach(
            name="Список ингредиентов",
            body="\n".join(f"{i.get_type()} - {i.get_name()} — {i.get_price()}" for i in ingredients),
            attachment_type=allure.attachment_type.TEXT
        )
        assert ingredients[index].get_name() == expected_name, f"Ингредиент {index} должен называться {expected_name}"

    @allure.title('Проверяем цену ингредиента: {param_id}')
    @pytest.mark.parametrize(
        'index, expected_price',
        [
            (0, 100),
            (1, 200),
            (2, 300),
            (3, 100),
            (4, 200),
            (5, 300),
        ],
        ids=[
            "1й - hot sauce — 100 руб.",
            "2й - sour cream — 200 руб.",
            "3й - chili sauce — 300 руб.",
            "4й - cutlet — 100 руб.",
            "5й - dinosaur — 200 руб.",
            "6й - sausage — 300 руб."
        ]
    )
    def test_ingredient_prices(self, index, expected_price):
        db = Database()
        ingredients = db.available_ingredients()
        allure.attach(
            name="Список ингредиентов",
            body="\n".join(f"{i.get_type()} - {i.get_name()} — {i.get_price()}" for i in ingredients),
            attachment_type=allure.attachment_type.TEXT
        )
        assert ingredients[index].get_price() == expected_price, f"Цена ингредиента {index} должна быть {expected_price}"

