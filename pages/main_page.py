import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_modal_locators import OrderModalLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Открыть главную страницу")
    def open(self):
        return self.open_page("main")

    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_main_page_loaded(self):
        self.wait.wait_for_page_load()
        assert self.is_visible(self.locators.CONSTRUCTOR_BUTTON), "Главная страница не загрузилась"
        return True

    @allure.step("Кликнуть на 'Конструктор'")
    def click_constructor(self):
        self.click(self.locators.CONSTRUCTOR_BUTTON)
        return self

    @allure.step("Кликнуть на 'Лента Заказов'")
    def click_order_feed(self):
        self.click(self.locators.ORDER_FEED_BUTTON)
        return self.wait_for_page_loaded()

    @allure.step("Кликнуть на 'Личный Кабинет'")
    def click_personal_account(self):
        self.click(self.locators.PERSONAL_ACCOUNT_BUTTON)
        return self.wait_for_page_loaded()

    @allure.step("Кликнуть на ингредиент с индексом {index}")
    def click_ingredient(self, index=0):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            self.execute_script("arguments[0].scrollIntoView(true);", ingredients[index])
            ingredients[index].click()
            self.wait.wait_for_element_visible(OrderModalLocators.INGREDIENT_DETAILS)
        return self

    @allure.step("Проверить видимость модального окна ингредиента")
    def is_ingredient_modal_visible(self):
        return self.is_visible(OrderModalLocators.INGREDIENT_DETAILS)

    @allure.step("Добавить ингредиент в конструктор по индексу {index}")
    def add_ingredient_to_constructor(self, index):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            # Перетаскиваем ингредиент в конструктор
            ingredient = ingredients[index]
            constructor_area = self.find_element(self.locators.CONSTRUCTOR_AREA)

            self.execute_script("""
                var dataTransfer = new DataTransfer();
                arguments[0].dispatchEvent(new DragEvent('dragstart', { dataTransfer: dataTransfer }));
                arguments[1].dispatchEvent(new DragEvent('drop', { dataTransfer: dataTransfer }));
                arguments[0].dispatchEvent(new DragEvent('dragend', { dataTransfer: dataTransfer }));
            """, ingredient, constructor_area)
        return self

    @allure.step("Получить счетчик ингредиента по индексу {index}")
    def get_ingredient_counter(self, index):
        ingredients = self.find_elements(self.locators.INGREDIENT_ITEM)
        if ingredients and index < len(ingredients):
            try:
                counter_element = ingredients[index].find_element(*self.locators.INGREDIENT_COUNTER)
                return int(counter_element.text)
            except:
                return 0
        return 0

    @allure.step("Кликнуть 'Оформить заказ'")
    def click_make_order(self):
        self.click(self.locators.ORDER_BUTTON)
        return self

    @allure.step("Проверить активность конструктора")
    def is_constructor_active(self):
        return self.is_present(self.locators.CONSTRUCTOR_ACTIVE)

    @allure.step("Проверить активность ленты заказов")
    def is_order_feed_active(self):
        return self.is_present(self.locators.ORDER_FEED_ACTIVE)

    @allure.step("Создать тестовый заказ")
    def create_test_order(self):
        # Добавляем несколько ингредиентов
        self.add_ingredient_to_constructor(0)  # Первая булка
        self.add_ingredient_to_constructor(5)  # Соус
        self.add_ingredient_to_constructor(10) # Начинка
        return self.click_make_order()

    @allure.step("Получить номер созданного заказа из модального окна")
    def get_created_order_number(self):
        try:
            order_number_element = self.find_element(OrderModalLocators.ORDER_NUMBER, timeout=10)
            return order_number_element.text
        except:
            return None

    @allure.step("Кликнуть на раздел 'Булки'")
    def click_buns_section(self):
        self.click(self.locators.BUNS_SECTION)
        return self

    @allure.step("Кликнуть на раздел 'Соусы'")
    def click_sauces_section(self):
        self.click(self.locators.SAUCES_SECTION)
        return self

    @allure.step("Кликнуть на раздел 'Начинки'")
    def click_fillings_section(self):
        self.click(self.locators.FILLINGS_SECTION)
        return self

    @allure.step("Проверить активность раздела 'Булки'")
    def is_buns_section_active(self):
        return self.is_present(self.locators.BUNS_SECTION_ACTIVE)

    @allure.step("Проверить активность раздела 'Соусы'")
    def is_sauces_section_active(self):
        return self.is_present(self.locators.SAUCES_SECTION_ACTIVE)

    @allure.step("Проверить активность раздела 'Начинки'")
    def is_fillings_section_active(self):
        return self.is_present(self.locators.FILLINGS_SECTION_ACTIVE)

    @allure.step("Проверить загрузку главной страницы")
    def is_main_page_loaded(self):
        return self.is_visible(self.locators.PAGE_TITLE)
