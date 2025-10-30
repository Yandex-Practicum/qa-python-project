from faker import Faker 
import random
fake = Faker()

bun_name = fake.word()
bun_price = fake.pyint(min_value=1, max_value=1000000)

type_list = ['Начинка', 'Соус']
ingredient_type = random.choice(type_list)
ingredient_name = f"Космический {fake.word()}"
ingredient_price = fake.pyint(min_value=1, max_value=1000000)

bun_list = [['black bun', 100], ['white bun', 200], ['red bun', 300]]
sauce_names_in_dtb = [['hot sauce', 'SAUCE', 100], ['sour cream', 'SAUCE', 200], ['chili sauce', 'SAUCE', 300]]
filling_names_in_dtb = [['cutlet', 'FILLING', 100], ['dinosaur', 'FILLING', 200], ['sausage', 'FILLING', 300]]
ingredients_list = [['hot sauce', 'SAUCE', 100], ['sour cream', 'SAUCE', 200], ['chili sauce', 'SAUCE', 300], ['cutlet', 'FILLING', 100], ['dinosaur', 'FILLING', 200], ['sausage', 'FILLING', 300]]