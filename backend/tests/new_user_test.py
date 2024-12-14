# test_user.py
import unittest
from unittest.mock import patch
from ..auth import new_user  

class TestNewUser(unittest.TestCase):
    @patch('builtins.input')
    def test_valid_names(self, mock_input):
        # This simulates user typing "John" then "Doe"
        mock_input.side_effect = ["John", "Doe"]
        
        # Run the function
        first, last = new_user(first_name='', last_name='')
        
        # Check if the function returns what we expect
        self.assertEqual(first, "John")
        self.assertEqual(last, "Doe")

if __name__ == '__main__':
    unittest.main()