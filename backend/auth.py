class User:
    """
    A class to manage user account creation and validation.
    Handles user's personal information, email, and password.
    """
    
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.email = None
        self.password = None

    def validate_names(self, first_name=None, last_name=None):
        """
        Accepts first name and last name from user input.
        Ensures both names are less than 50 characters long.

        Args:
            first_name (str): Placeholder argument for first name.
            last_name (str): Placeholder argument for last name.

        Returns:
            tuple: first_name, last_name

        Raises:
            ValueError: If invalid input is provided.
        """
        try:
            first_name = input("Enter your first name: ")
            if len(first_name) > 50:
                print("Name must be less than 50 letters")
                return False
            
            last_name = input("Enter your last name: ")
            if len(last_name) > 50:
                print("Name must be less than 50 letters")
                return False

            self.first_name = first_name
            self.last_name = last_name
            return True

        except ValueError:
            print("Please enter valid text")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def validate_email(self):
        """
        Validates and sets the user's email address.
        
        Returns:
            bool: True if email is valid, False otherwise
            
        Raises:
            Exception: If an error occurs during validation
        """
        try:
            email = input("Enter your email address: ")
            
            # Basic email validation
            if '@' not in email or '.' not in email:
                print("Invalid email format. Must contain '@' and '.'")
                return False
                
            # Check email length
            if len(email) > 100:
                print("Email must be less than 100 characters")
                return False
            
            self.email = email
            return True

        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def create_password(self):
        """
        Creates and validates a new password based on the following rules:
        - Minimum 8 characters long
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one number
        - At least one special character (!@#$%^&*()_+-=[]{}|;:,.<>?)

        Returns:
            bool: True if password creation is successful, False otherwise

        Raises:
            ValueError: If invalid input is provided
        """
        while True:
            try:
                password = input("Create a password: ")
                
                # Check minimum length
                if len(password) < 8:
                    print("Password must be at least 8 characters long")
                    continue
                
                # Check for uppercase
                if not any(c.isupper() for c in password):
                    print("Password must contain at least one uppercase letter")
                    continue
                
                # Check for lowercase
                if not any(c.islower() for c in password):
                    print("Password must contain at least one lowercase letter")
                    continue
                
                # Check for numbers
                if not any(c.isdigit() for c in password):
                    print("Password must contain at least one number")
                    continue
                
                # Check for special characters
                special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
                if not any(c in special_chars for c in password):
                    print("Password must contain at least one special character")
                    continue
                
                # If all checks pass, confirm password
                confirm_password = input("Confirm your password: ")
                if password != confirm_password:
                    print("Passwords do not match")
                    continue
                
                self.password = password
                return True

            except Exception as e:
                print(f"An error occurred: {e}")
                return False

    def create_account(self):
        """
        Main method to handle the account creation process.
        Coordinates the validation of names, email, and password.
        
        Returns:
            bool: True if account creation is successful, False otherwise
        """
        if self.validate_names() and self.validate_email() and self.create_password():
            print("Account created successfully!")
            return True
        else:
            print("Account creation failed")
            return False

def main():
    """
    Main function to run the user account creation process.
    """
    user = User()
    user.create_account()

if __name__ == "__main__":
    main()