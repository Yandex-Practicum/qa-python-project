class BunTestData:
 
    VALID_BUN = {"name": "classic bun", "price": 111.0}
    
   
    MIN_PRICE_BUN = {"name": "min price bun", "price": 0.0}
    MAX_PRICE_BUN = {"name": "max price bun", "price": 1000000.0}
    
    
    EMPTY_NAME_BUN = {"name": "", "price": 100.0}
    NEGATIVE_PRICE_BUN = {"name": "negative price", "price": -50.0}
    
    @staticmethod
    def get_valid_bun():
        return BunTestData.VALID_BUN.copy()