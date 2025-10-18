# Установка зависимостей
pip install -r requirements.txt

# Запуск всех тестов с покрытием
pytest --cov=praktikum --cov-report=html

# Запуск конкретного тестового файла
pytest tests/bun_test.py -v

# Запуск с детальным отчетом о покрытии
pytest --cov=praktikum --cov-report=term-missing

# Генерация XML отчета для CI/CD
pytest --cov=praktikum --cov-report=xml
