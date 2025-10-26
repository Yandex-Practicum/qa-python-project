import sys
import os

# Добавляем путь до папки 'praktikum' в системный путь поиска модулей
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'praktikum')))

# Теперь можно импортировать модули из папки praktikum
from praktikum.burger import Burger

import pytest
from unittest.mock import Mock

@pytest.fixture()
def buns_with_ingred():
    "Фикстура для мок-объектов булок и ингредиентов"

    # Моки для булок
    mock_bun1 = Mock()
    mock_bun1.get_name.return_value = 'Флюоресцентная булка R2-D3'
    mock_bun1.get_price.return_value = 988
    mock_bun1.get_type.return_value = 'BUN'

    mock_bun2 = Mock()
    mock_bun2.get_name.return_value = 'Краторная булка N-200i'
    mock_bun2.get_price.return_value = 1255
    mock_bun2.get_type.return_value = 'BUN'

    # Моки для соусов (ингредиенты)
    mock_sauce1 = Mock()
    mock_sauce1.get_name.return_value = 'Соус Spicy-X'
    mock_sauce1.get_price.return_value = 90
    mock_sauce1.get_type.return_value = 'SAUCE'

    mock_sauce2 = Mock()
    mock_sauce2.get_name.return_value = 'Соус фирменный Space Sauce'
    mock_sauce2.get_price.return_value = 80
    mock_sauce2.get_type.return_value = 'SAUCE'

    # Моки для начинок (ингредиенты)
    mock_filling1 = Mock()
    mock_filling1.get_name.return_value = 'Мясо бессмертных моллюсков Protostomia'
    mock_filling1.get_price.return_value = 1337
    mock_filling1.get_type.return_value = 'FILLING'

    mock_filling2 = Mock()
    mock_filling2.get_name.return_value = 'Говяжий метеорит (отбивная)'
    mock_filling2.get_price.return_value = 3000
    mock_filling2.get_type.return_value = 'FILLING'

    # Возвращаем список с булками, соусами и начинками
    return [
        [mock_bun1, mock_bun2],      # Булки
        [mock_sauce1, mock_sauce2],  # Соусы
        [mock_filling1, mock_filling2]  # Начинки
    ]
