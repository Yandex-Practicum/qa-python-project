import uuid
from unittest.mock import Mock


def get_bun_mock() -> Mock:
    mock = Mock()

    mock.get_name.return_value = f"fake_bun_{uuid.uuid4()}"
    mock.get_price.return_value = 1
    mock.get_type.return_value = "fake_bun_type"

    return mock


if __name__ == "__main__":
    print(uuid.uuid4())
