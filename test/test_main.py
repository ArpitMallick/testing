# tests/test_main.py

import pytest
from unittest.mock import patch
import src.main as main_module

def test_main_prints_hello_world():
    with patch('builtins.print') as mock_print:
        main_module.main()
        mock_print.assert_called_once_with("Hello, World!")

