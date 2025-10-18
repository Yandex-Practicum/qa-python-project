# UI Автотесты для Stellar Burgers
## 📋 Структура проекта
ui-tests/
├── pages/ # Классы Page Object
│ ├── base_page.py
│ ├── main_page.py
│ ├── login_page.py
│ ├── order_feed_page.py
│ └── order_modal.py
├── locators/ # Локаторы элементов
│ ├── main_page_locators.py
│ ├── login_page_locators.py
│ ├── order_feed_locators.py
│ └── order_modal_locators.py
├── helpers/ # Вспомогательные классы
│ ├── url_helper.py
│ ├── data_helper.py
│ └── wait_helper.py
├── tests/ # Тестовые сценарии
│ ├── test_main_functionality.py
│ ├── test_order_feed.py
│ ├── test_additional_scenarios.py
│ └── conftest.py
├── requirements.txt # Зависимости
├── pytest.ini # Конфигурация Pytest
└── README.md # Этот файл

## 🚀 Тестируемая функциональность

### Основная функциональность
- ✅ Переход по клику на «Конструктор»
- ✅ Переход по клику на «Лента Заказов»
- ✅ Открытие модального окна с деталями ингредиента
- ✅ Закрытие модального окна
- ✅ Увеличение счетчика ингредиента
- ✅ Переключение разделов конструктора

### Лента заказов
- ✅ Увеличение счетчика «Выполнено за всё время»
- ✅ Увеличение счетчика «Выполнено за сегодня»
- ✅ Появление заказа в разделе «В работе»
- ✅ Обновление счетчиков в реальном времени
- ✅ Навигация между разделами

## 🛠 Установка

### Предварительные требования
- Python 3.8 или выше
- pip (менеджер пакетов Python)
- Google Chrome или Mozilla Firefox

### 1. Клонирование репозитория
```bash
git clone <URL-репозитория>
cd ui-tests
### 2. Установка зависимостей
pip install -r requirements.txt
### 3. Запуск всех тестов
bash
pytest tests/ -v
### 4. Запуск в разных браузерах
# Chrome (по умолчанию)
pytest tests/ -v

# Firefox
pytest tests/ --browser=firefox -v
### 5. Запуск с Allure отчетами
# Генерация результатов Allure
pytest tests/ --alluredir=allure-results
