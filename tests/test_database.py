import allure


class TestDatabase:
    # В классе Database по сути тестировать нечего. В реальном проекте этот
    # класс (Database) должен обращаться к базе, и методы available_buns и
    # available_ingredients, соответственно, селектить данные из БД.
    # Мы не можем протестировать набор данных из БД, так как он постоянно меняется, но можем проверить
    #корректность работы метода, а именно что возвращается list.
    #Так как в реальном проекте метод будет обращаться в БД и селектить оттуда, возвращая результат,
    #проверять, что метод возвращает список равный списку из БД не вижу смысла.

    @allure.title("Проверка типа данных переменной available_buns")
    def test_available_buns(self, test_database):
        assert isinstance(test_database.available_buns(), list)

    @allure.title("Проверка типа данных переменной available_ingredients")
    def test_available_ingredients(self, test_database):
        assert isinstance(test_database.available_ingredients(), list)