import pytest
from typing import List, Dict
from Diplom_1.bun import Bun
from Diplom_1.database import Database

@pytest.fixture
def database():
    """
    Фикстура для создания экземпляра Database.
    """
    return Database()

@pytest.fixture
def buns_by_name(database: Database) -> Dict[str, Bun]:
    """Фикстура, возвращающая словарь булок по имени."""
    return {bun.name: bun for bun in database.available_buns()}

class TestBun:

    @pytest.fixture
    def bun(self):
        """
        Фикстура для создания экземпляра Bun (по умолчанию).
        """
        return Bun("default bun", 0)  # Создаем Bun с какими-то значениями по умолчанию


    @pytest.mark.parametrize(
        "bun_name",
        [
            ("black bun"),
            ("white bun"),
            ("red bun")
        ],
    )
    def test_get_name_parametrize(self, buns_by_name: Dict[str, Bun], bun_name: str):
        """
        Проверяет правильность работы метода get_name().
        """
        found_bun = buns_by_name.get(bun_name)

        assert found_bun is not None, f"Булка с именем '{bun_name}' не найдена в базе данных."
        assert found_bun.get_name() == bun_name


    @pytest.mark.parametrize(
        "bun_name, bun_price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300)
        ],
    )
    def test_get_price_parametrize(self, buns_by_name: Dict[str, Bun], bun_name: str, bun_price: int):
        """
        Проверяет правильность работы метода get_price().
        """
        found_bun = buns_by_name.get(bun_name)

        # Проверяем, что булка найдена и ее цена соответствует ожидаемому
        assert found_bun is not None, f"Булка с именем '{bun_name}' не найдена в базе данных."
        assert found_bun.get_price() == bun_price, f"Цена булки '{bun_name}' не соответствует ожидаемой."
