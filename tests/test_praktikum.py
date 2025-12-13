"""Тесты для основного модуля praktikum"""
import pytest
import sys
from io import StringIO

def test_main_executes_without_error():
    """Тест что main выполняется без ошибок"""
    from praktikum.praktikum import main    
    main()

def test_main_has_output(capsys):
    """Тест что main выводит результат"""
    from praktikum.praktikum import main
    
    main()
    captured = capsys.readouterr()    
    
    assert captured.out != ""