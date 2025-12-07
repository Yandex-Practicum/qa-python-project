from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Тестовые данные для get_receipt
GET_RECEIPT_TEST_DATA = [
    {
        "name": "Бургер с соусом и котлетой",
        "bun_name": "black bun",
        "ingredients": [
            (INGREDIENT_TYPE_SAUCE, "hot sauce"),
            (INGREDIENT_TYPE_FILLING, "cutlet")
        ],
        "expected_lines": [
            "(==== black bun ====)",
            "= sauce hot sauce =",
            "= filling cutlet =",
            "(==== black bun ====)",
            "",
            "Price: 0"
        ]
    },
    {
        "name": "Бургер с динозавром и сметаной",
        "bun_name": "white bun",
        "ingredients": [
            (INGREDIENT_TYPE_FILLING, "dinosaur"),
            (INGREDIENT_TYPE_SAUCE, "sour cream")
        ],
        "expected_lines": [
            "(==== white bun ====)",
            "= filling dinosaur =",
            "= sauce sour cream =",
            "(==== white bun ====)",
            "",
            "Price: 0"
        ]
    }
]

# Тестовые данные для get_price
GET_PRICE_TEST_DATA = [
    {
        "name": "Булочка за 100 и два ингредиента",
        "bun_price": 100,
        "ingredient_prices": [50, 75],
        "expected_total": 325  
    },
    {
        "name": "Булочка за 50 и три ингредиента",
        "bun_price": 50,
        "ingredient_prices": [25, 30, 45],
        "expected_total": 200  
    },
    {
        "name": "Только булочка",
        "bun_price": 200,
        "ingredient_prices": [],
        "expected_total": 400  
    },
    {
        "name": "Булочка бесплатная с платными ингредиентами",
        "bun_price": 0,
        "ingredient_prices": [10, 20],
        "expected_total": 30  
    }
]