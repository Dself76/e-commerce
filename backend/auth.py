def new_user(first_name, last_name):
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
        
        last_name = input("Enter your last name: ")
        if len(last_name) > 50:
            print("Name must be less than 50 letters")

        return first_name, last_name

    except ValueError:
        print("Please enter valid text")
    except Exception as e:
        print(f"An error occurred: {e}")
