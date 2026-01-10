
from database import  Database


class Helpers:
    database = Database()
    list_buns = database.available_buns()
    list_ingredients = database.available_ingredients()
    list_names = [bun.get_name() for bun in list_buns]
    ingr_names = [ingredient.get_name() for ingredient in list_ingredients]
