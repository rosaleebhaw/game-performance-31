def validate_input(user_input):
    """
    Validate the user input for game controls.
    Args:
        user_input (str): The input provided by the user.
    Returns:
        bool: True if input is valid, False otherwise.
    """
    valid_inputs = {'w', 'a', 's', 'd', 'q', 'e'}
    return user_input in valid_inputs

def main_game_loop():
    """
    Main processing loop for the game.
    """
    while True:
        user_input = input("Enter your command (w/a/s/d/q/e): ").strip().lower()
        if validate_input(user_input):
            print(f"Valid input detected: {user_input}")
            # Here would go the code to process the command
        else:
            print(f"Invalid input: '{user_input}'. Please try again.")

if __name__ == '__main__':
    main_game_loop()