import unittest


from unittest.mock import patch
import io
import sys

class TestLab1_1(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '1'])
    def test_sum(self, mock_input):
        # Capture stdout to verify output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Import and run the program
        from lab1_1 import main
        main()

        # Get the output
        output = captured_output.getvalue()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Check if sum is correct (1 + 1 = 2)
        self.assertIn('Sum: 2.0', output)
        self.assertIn('Difference: 0.0', output)

    @patch('builtins.input', side_effect=['10', '4'])
    def test_difference(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        from lab1_1 import main
        main()

        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertIn('Sum: 14.0', output)
        # Check if difference is correct (10 - 4 = 6)
        self.assertIn('Difference: 6.0', output)

if __name__ == '__main__':
    unittest.main()