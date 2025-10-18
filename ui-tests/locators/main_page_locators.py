from selenium.webdriver.common.by import By


class MainPageLocators:
    # Навигация
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")

    # Активные состояния навигации
    CONSTRUCTOR_ACTIVE = (By.XPATH, "//a[.//p[text()='Конструктор'] and contains(@class, 'active')]")
    ORDER_FEED_ACTIVE = (By.XPATH, "//a[.//p[text()='Лента Заказов'] and contains(@class, 'active')]")

    # Конструктор бургеров
    INGREDIENTS_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients')]")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, ".//div[contains(@class, 'counter_counter')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")

    # Активные разделы
    BUNS_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Булки']")
    SAUCES_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Соусы']")
    FILLINGS_SECTION_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Начинки']")

    # Ингредиенты по категориям
    BUNS_INGREDIENTS = (By.XPATH, "//h2[text()='Булки']/following-sibling::ul//a")
    SAUCES_INGREDIENTS = (By.XPATH, "//h2[text()='Соусы']/following-sibling::ul//a")
    FILLINGS_INGREDIENTS = (By.XPATH, "//h2[text()='Начинки']/following-sibling::ul//a")

    # Область конструктора
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    CONSTRUCTOR_ITEMS = (By.XPATH, "//div[contains(@class, 'BurgerConstructor_basket')]//div[contains(@class, 'BurgerConstructor_element')]")

    # Заголовки
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
