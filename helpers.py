from data import Data


class Helpers:

    def price_receipt(self):
        price_receipt = 2 * Data.MOCK_BUN_PRICE_VALUE + Data.MOCK_INGREDIENT_PRICE_VALUE
        return price_receipt
