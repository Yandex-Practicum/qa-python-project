import uuid
from unittest.mock import Mock


def get_ingredient_mock() -> Mock:
    mock = Mock()

    mock.get_name.return_value = f"fake_ingredient_{uuid.uuid4()}"
    mock.get_price.return_value = 1
    mock.get_type.return_value = "fake_ingredient_type"

    return mock
