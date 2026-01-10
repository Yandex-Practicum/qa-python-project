from praktikum import main

def test_main_function(capfd):
    """
    Тестируем выполнение функции main() и проверяем, что рецепт выводится в консоль.
    Используем capfd для захвата вывода в stdout.
    """
    main()  # Запускаем функцию main()

    # Захватываем вывод в stdout
    captured = capfd.readouterr()

    # Проверяем, что в выводе есть ключевые части рецепта
    assert "(==== black bun ====)" in captured.out
    assert "= sauce sour cream =" in captured.out
    assert "= filling cutlet =" in captured.out
    assert "Price:" in captured.out
