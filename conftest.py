import sys
import os
import pytest

from helpers import Help
from praktikum.bun import Bun
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


#фикстура по созданию булочки с именем и ценой из доступных булочек
@pytest.fixture
def bun_option():
    help = Help()
    bun_option = help.bun_option_method()
    name_bun_option = bun_option.name
    price_bun_option = bun_option.price
    return Bun(name_bun_option, price_bun_option)
