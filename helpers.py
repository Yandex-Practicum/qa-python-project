import random

from praktikum.database import Database


class Help:
    #рандомный выбор из доступных булочек
    def bun_option_method(self):
        data_base = Database()
        return random.choice(data_base.available_buns())