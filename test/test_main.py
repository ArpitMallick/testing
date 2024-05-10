# tests/test_main.py

import unittest
from unittest.mock import patch
import src.main as main_module

class TestMain(unittest.TestCase):
    @patch('builtins.print')
    def test_main_prints_hello_world(self, mock_print):
        main_module.main()
        mock_print.assert_called_once_with("Hello, World!")

if __name__ == '__main__':
    unittest.main()

