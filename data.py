class BunTestData:
    buns = ['Лунная Лепешка', 'Meteoric Softness', 'Неизведанный Нахлыст 228']
    price = [500, 0, -500]


class IngredientTestData:
    price = [500, 0, -500]
    type = ['Соусы', 'Toppings', '01 and 02']
    ingredients = ['Марсианский Маринад', 'Планетарный Песто', 'алактическая Гауда']


class BurgerTestData:
    receipt = (f'(==== {BunTestData.buns[0]} ====)\n= {IngredientTestData.type[0].lower()} '
               f'{IngredientTestData.ingredients[0]} =\n(==== {BunTestData.buns[0]} ====)\n\nPrice: {BunTestData.price[0]*3}')