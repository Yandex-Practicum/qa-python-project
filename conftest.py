from unittest.mock import Mock

import pytest


@pytest.fixture(scope='function')
def ingridient_mock():
     ingridient = Mock()
     ingridient.get_type.return_value = 'Соус'
     ingridient.get_name.return_value = 'Гарнир'
     ingridient.get_price.return_value = 10
     return ingridient

@pytest.fixture(scope='function')
def bun_mock():
     bun = Mock()
     bun.get_name.return_value = 'Кунжут'
     bun.get_price.return_value = 10
     return bun