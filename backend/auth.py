def new_user(first_name,last_name):
    try:

        first_name=input('')
        if len(first_name) > 50:
            print('Name must be less than 50 letters')
        
        last_name = input('')
        if len(first_name) > 50:
            print('Name must be less than 50 letters')

        return first_name, last_name
    except ValueError:
        print("Please enter valid text")
    except Exception as e:
        print(f"An error occurred: {e}")


