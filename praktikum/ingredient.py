class Ingredient:
    """
    Модель ингредиента.
    Ингредиент: начинка или соус.
    У ингредиента есть тип (начинка или соус), название и цена.
    """

    def __init__(self, ingredient_type: str, name: str, price: float):
        if not name or price < 0 or not ingredient_type:
            raise ValueError("Неверные данные для ингредиента.")
        
        self.type = ingredient_type
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def get_name(self) -> str:
        return self.name

    def get_type(self) -> str:
        return self.type
