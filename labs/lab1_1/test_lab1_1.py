import unittest
from unittest.mock import patch
import io
import sys

class TestLab1_1(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '1'])
    def test_sum(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        from lab1_1 import main
        main()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

        self.assertIn('Sum: 2.0', output, "Expected sum of 1 + 1 to be 2.0")
        self.assertIn('Difference: 0.0', output, "Expected difference of 1 - 1 to be 0.0")

    @patch('builtins.input', side_effect=['10', '4'])
    def test_difference(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        from lab1_1 import main
        main()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

        self.assertIn('Sum: 14.0', output, "Expected sum of 10 + 4 to be 14.0")
        self.assertIn('Difference: 6.0', output, "Expected difference of 10 - 4 to be 6.0")

if __name__ == '__main__':
    unittest.main()