class Bun:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Ingredient:
    def __init__(self, name, ingredient_type, price):
        self.name = name
        self.type = ingredient_type
        self.price = price

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_price(self):
        return self.price

class Burger:
    def __init__(self):
        self.bun = None
        self.ingredients = []

    def set_buns(self, bun):
        self.bun = bun

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        self.ingredients.remove(ingredient)

    def move_ingredient(self, old_index, new_index):
        self.ingredients.insert(new_index, self.ingredients.pop(old_index))

    def get_price(self):
        total = 0
        if self.bun:
            total += self.bun.get_price() * 2
        for ing in self.ingredients:
            total += ing.get_price()
        return total

    def get_receipt(self):
        lines = []
        lines.append(f"(==== {self.bun.get_name()} ====)")
        for ing in self.ingredients:
            lines.append(f"= {str(ing.get_type()).lower()} {ing.get_name()} =")
        lines.append(f"(==== {self.bun.get_name()} ====)")
        lines.append(f"Price: {self.get_price()}")
        return "\n".join(lines)