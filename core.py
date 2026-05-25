import sys

class GameInputError(Exception):
    pass

def validate_input(user_input):
    if not isinstance(user_input, str) or not user_input.strip():
        raise GameInputError('Input must be a non-empty string.')

    # Add more validation rules as needed

    return user_input.strip()

def main():
    while True:
        try:
            user_input = input('Enter a command: ')
            valid_input = validate_input(user_input)
            # Process the valid input here
            print(f'Processing command: {valid_input}')
        except GameInputError as e:
            print(f'Input Error: {e}')
        except KeyboardInterrupt:
            print('\nExiting game. Goodbye!')
            sys.exit(0)

if __name__ == '__main__':
    main()