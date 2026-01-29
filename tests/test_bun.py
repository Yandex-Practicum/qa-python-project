import pytest
from praktikum.bun import Bun
from helpers.helpers import BunTestData as TestData


class TestBun:
    @pytest.mark.parametrize('test_param', [
        'name',
        'price'
    ])
    def test_class_init_data_create_if_set_correctly(self, test_param):
        bun = Bun(TestData.name, TestData.price)
        assert getattr(bun, test_param) == getattr(TestData, test_param)

    @pytest.mark.parametrize('test_param', [
        'name',
        'price'
    ])
    def test_class_getters_return_value(self, test_param):
        bun = Bun(TestData.name, TestData.price)
        assert getattr(bun, f'get_{test_param}')() == getattr(TestData, test_param)
