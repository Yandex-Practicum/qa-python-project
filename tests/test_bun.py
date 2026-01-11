import allure
from ya_praktikum.bun import Bun

class TestBun:
    @allure.title('Проверка инициализации булочки')
    @allure.description('Тест проверяет, что булочка инициализируется с правильными данными')
    def test_init_bun(self):
        bun = Bun('Булочка', 100)
        assert bun.get_name() == 'Булочка', f'Ожидается название: Булочка, получено: {bun.get_name()}'
        assert bun.get_price() == 100, f'Ожидается цена: 100, получено: {bun.get_price()}'
        print('\nТест пройден!')
        print(f'Название булочки  - {bun.get_name()}, цена - {bun.get_price()}')

    @allure.title('Проверка изменения названии булочки')
    @allure.description('Тест проверяет, что можно изменить название булочки')
    def test_name_change(self, create_bun):
        bun = create_bun
        bun.name = 'Булка'
        assert bun.get_name() == 'Булка', f'Ожидается название: Булка, получено: {bun.get_name()}'
        print('\nТест пройден!')
        print(f'Название булочки  - {bun.get_name()}')

    @allure.title('Проверка изменения цены булочки')
    @allure.description('Тест проверяет, что можно изменить цену булочки')
    def test_price_change(self, create_bun): #Изменение цены булочки
        bun = create_bun
        bun.price = 500
        assert bun.get_price() == 500, f'Ожидается цена: 500, получено:  {bun.get_price()}'
        print('\nТест пройден!')
        print(f'Цена  - {bun.get_price()}')



