while True:
    try:
        # Accept input from the user
        user_input = input("Please enter an integer: ")
        
        # Try to convert input to an integer
        user_input = int(user_input)
        
        # If conversion is successful, exit the loop
        print(f"Thank you! You've entered the integer: {user_input}")
        break 
    
    except ValueError:
        print("Error: That's not an integer. Please try again.")
