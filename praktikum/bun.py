class Bun:
    """
    Модель булки.
    У булки есть название и цена.
    """

    def __init__(self, name: str, price: float):
        if not name or price < 0:
            raise ValueError("Неверные данные для булки.")
        
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price
