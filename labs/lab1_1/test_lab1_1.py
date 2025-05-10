
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

        self.assertIn('Sum: 8.0', output, "Expected sum of 5 + 3 to be 8.0")
        self.assertIn('Difference: 2.0', output, "Expected difference of 5 - 3 to be 2.0")

    @patch('builtins.input', side_effect=['7', '2'])
    def test_difference(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        from lab1_1 import main
        main()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

        self.assertIn('Sum: 9.0', output, "Expected sum of 7 + 2 to be 9.0")
        self.assertIn('Difference: 5.0', output, "Expected difference of 7 - 2 to be 5.0")

if __name__ == '__main__':
    unittest.main()
