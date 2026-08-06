import pytest
from unittest.mock import patch

from praktikum.praktikum import main

def test_practikum_main_execution():

    with patch("builtins.print") as mock_print:
       
        main()
        
        mock_print.assert_called_once()
