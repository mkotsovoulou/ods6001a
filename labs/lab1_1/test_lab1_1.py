
import unittest
from unittest.mock import patch
import io
import sys

class TestLab1_1(unittest.TestCase):
    @patch('builtins.input', side_effect=['5', '3'])
    def test_sum(self, mock_input):
        # Capture stdout to verify output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Import and run the program
        import lab1_1
        
        # Get the output
        output = captured_output.getvalue()
        
        # Reset stdout
        sys.stdout = sys.__stdout__
        
        # Check if sum is correct (5 + 3 = 8)
        self.assertIn('Sum: 8.0', output)

    @patch('builtins.input', side_effect=['10', '4'])
    def test_difference(self, mock_input):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        import lab1_1
        
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        
        # Check if difference is correct (10 - 4 = 6)
        self.assertIn('Difference: 6.0', output)

if __name__ == '__main__':
    unittest.main()
