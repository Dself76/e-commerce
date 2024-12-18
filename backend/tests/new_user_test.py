import unittest
from unittest.mock import patch
import sys
sys.path.insert(0, 'C:/Users/dself/OneDrive/Programming/e-commerce/backend')
from auth import User

class TestUserUnit(unittest.TestCase):
    """
    Unit tests for the User class to validate individual components like name and password.
    """
    
    def setUp(self):
        """Set up a new User instance before each test method."""
        self.user = User()

    @patch('builtins.input')
    def test_valid_names(self, mock_input):
        """
        Test user name validation for valid inputs.
        """
        mock_input.side_effect = ["John", "Doe"]
        result = self.user.validate_names()
        self.assertTrue(result)
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    @patch('builtins.input')
    def test_name_empty(self, mock_input):
        """
        Test user name validation rejects empty first name.
        """
        mock_input.side_effect = ["", "Doe"]
        result = self.user.validate_names()
        self.assertFalse(result)

    @patch('builtins.input')
    def test_password_all_requirements(self, mock_input):
        """
        Test password validation when all requirements are met.
        """
        mock_input.side_effect = ["Testing123!", "Testing123!"]
        result = self.user.create_password()
        self.assertTrue(result)

    @patch('builtins.input')
    def test_password_requirements(self, mock_input):
        """
        Test password validation for various missing requirements.
        """
        test_cases = [
            ("short1!", "short1!"),  # Too short
            ("nouppercase123!", "nouppercase123!"),  # No uppercase letter
            ("NOLOWERCASE123!", "NOLOWERCASE123!"),  # No lowercase letter
            ("NoSpecialChar123", "NoSpecialChar123"),  # No special character
            ("NoNumber!", "NoNumber!"),  # No numeral
        ]
        
        for password, confirm in test_cases:
            mock_input.side_effect = [password, confirm]
            result = self.user.create_password()
            self.assertFalse(result, f"Failed for: {password}")

class TestUserIntegration(unittest.TestCase):
    """
    Integration tests for the User class to validate the complete registration process.
    """
    
    def setUp(self):
        """Set up a new User instance before each test method."""
        self.user = User()

    @patch('builtins.input')
    def test_full_registration_process(self, mock_input):
        """
        Test the complete registration process from name input to password confirmation.
        """
        mock_input.side_effect = ["John", "Doe", "john@example.com", "Testing123!", "Testing123!"]
        name_result = self.user.validate_names()
        email_result = self.user.validate_email()
        password_result = self.user.create_password()
        
        self.assertTrue(name_result and email_result and password_result)
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "john@example.com")
        self.assertIsNotNone(self.user.password)

class TestUserValidation(unittest.TestCase):
    """
    Validation tests for the User class to verify correct handling of invalid email formats.
    """
    
    def setUp(self):
        """Set up a new User instance before each test method."""
        self.user = User()

    @patch('builtins.input')
    def test_email_validation(self, mock_input):
        """
        Test email format validation to ensure various invalid formats are correctly rejected.
        """
        invalid_emails = [
            "notanemail", "@nodomain", "no@domain@test", "no.domain.com", "@.", "a" * 101 + "@test.com"
        ]
        
        for email in invalid_emails:
            mock_input.side_effect = [email]
            result = self.user.validate_email()
            self.assertFalse(result, f"Failed for: {email}")

if __name__ == '__main__':
    unittest.main()
