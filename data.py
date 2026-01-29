import random


class DataBun:
    name = ['delicious', 'soft']
    price = [100, 120]

    @classmethod
    def get_data_bun(cls):
        return random.choice(cls.name), random.choice(cls.price)


class DataIngredient:
    name = ['regular', 'traditional']
    price = [50, 70]
    type = ['sauce', 'filling']

    @classmethod
    def get_data_ingredient(cls):
        return random.choice(cls.name), random.choice(cls.price), random.choice(cls.type)
