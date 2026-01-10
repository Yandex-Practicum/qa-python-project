import pytest

from practicum.bun import Bun
import test_data


class TestBun:

    @pytest.mark.parametrize('bun', test_data.BUN_CORRECT_SET, indirect=True)
    def test_get_name_type(self, bun):
        # Проверка метода get_name
        assert isinstance(bun.get_name(), str), "Имя должно быть строкой"

    @pytest.mark.parametrize('bun', test_data.BUN_CORRECT_SET, indirect=True)
    def test_get_price_type(self, bun):
        # Проверка метода get_price
        assert isinstance(bun.get_price(), float) or isinstance(bun.get_price(),
                                                                int), "Цена должна быть числовым значением"

    @pytest.mark.parametrize('bun', test_data.BUN_CORRECT_SET, indirect=True)
    def test_bun_initialization(self, bun):
        # Проверка инициализации объекта Bun
        assert bun.get_name() in ["Сдобная булочка", "Wheat bun", "Ржаная булочка_1"], ("Ошибка при инициализациия name"
                                                                                        "объекта Bun")
        assert bun.get_price() in [50.0, 30, 25.0], "Ошибка при инициализациия price объекта Bun!"

    @pytest.mark.parametrize('bun', test_data.BUN_INCORRECT_SET, indirect=True)
    def test_bun_wrong_type_initialization(self, bun):
        # Проверка на отсутствие инициализации объекта Bun при некорректных значениях
        assert bun.get_name() not in [123, None], "Имя инициализируется неверным типом!"

        assert bun.get_price() not in [None, "100", [1, 2], {"1": 1.0, "2": 2}], ("Цена инициализируется неверным "
                                                                                  "типом!")

    def test_price_non_negative(self):
        # Проверка, что цена не может быть отрицательной или нулевой в рамках верного типа
        with pytest.raises(ValueError):
            Bun(name="Неправильная булочка", price=-10.0), "Цена не может быть отрицательной!"
        with pytest.raises(ValueError):
            Bun(name="Неправильная булочка", price=0.0), "Цена не может быть нулевой!"

    def test_name_non_empty(self):
        # Проверка, что имя не может быть пустым в рамках верного типа
        with pytest.raises(ValueError):
            Bun(name="", price=10.0), "Имя не может быть пустым!"
