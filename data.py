import helpers
import random

buns = ["black bun", "white bun", "red bun"]
random_bun = random.choice(buns)

sauces = ["hot sauce", "sour cream", "chili sauce"]
random_sauce = random.choice(sauces)
fillings = ["cutlet", "sour cream", "chili sauce"]
random_filling = random.choice(fillings)

random_price_int = helpers.random_price_int()
random_price_float = helpers.random_price_float()