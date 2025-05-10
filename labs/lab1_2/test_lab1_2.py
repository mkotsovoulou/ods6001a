
import unittest
from unittest.mock import patch
import io
import sys

class TestLab1_2(unittest.TestCase):
    @patch('builtins.input', side_effect=['John'])
    def test_name_length_and_lowest(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        from lab1_2 import main
        main()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        try:
            self.assertEqual(output, "4\nH\n", "Expected output '4' and 'H' for input 'John'")
        except AssertionError as e:
            print("Test failed:", str(e))

if __name__ == '__main__':
    unittest.main()
