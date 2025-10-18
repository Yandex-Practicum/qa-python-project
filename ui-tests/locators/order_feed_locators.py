from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Основные элементы ленты заказов
    ORDER_FEED_SECTION = (By.XPATH, "//section[contains(@class, 'OrderFeed')]")
    ORDER_FEED_CONTAINER = (By.XPATH, "//div[contains(@class, 'OrderFeed_container')]")

    # Счетчики заказов
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[contains(@class, 'digits-large')]")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[contains(@class, 'digits-large')]")

    # Заказы в работе
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]//li[contains(@class, 'OrderFeed_number')]")
    IN_PROGRESS_SECTION = (By.XPATH, "//div[contains(@class, 'OrderFeed_inProgress')]")

    # Список заказов
    ORDER_ITEMS = (By.XPATH, "//div[contains(@class, 'OrderHistory_list')]//li | //div[contains(@class, 'OrderFeed_orderList')]//li")
    ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'digits-default')]")

    # Модальное окно заказа
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//p[contains(@class, 'digits-large')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'Modal_modal')]//button[contains(@class, 'Modal_modal__close')]")
