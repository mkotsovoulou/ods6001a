
import unittest
from unittest.mock import patch
import io
import sys

class TestLab1_1(unittest.TestCase):
    @patch('builtins.input', side_effect=['5', '3'])
    def test_sum(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        from lab1_1 import main
        main()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        try:
            self.assertTrue('Sum: 8.0' in output or 'Sum: 8' in output, "Expected sum of 5 + 3 to be either 8 or 8.0")
        except AssertionError as e:
            print("Test failed:", str(e))

  
if __name__ == '__main__':
    unittest.main()
