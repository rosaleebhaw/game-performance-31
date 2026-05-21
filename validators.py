import re

def is_valid_username(username):
    """
    Validates if the username meets the criteria:
    - Length between 3 to 20 characters
    - Only alphanumeric characters allowed
    """
    return bool(re.match('^[A-Za-z0-9]{3,20}$', username))


def is_valid_email(email):
    """
    Checks if the provided email address is in a valid format.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_valid_password(password):
    """
    Validates the password strength:
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    if len(password) < 8:
        return False
    if not re.search('[A-Z]', password):
        return False
    if not re.search('[a-z]', password):
        return False
    if not re.search('[0-9]', password):
        return False
    if not re.search('[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True


def are_tokens_valid(tokens):
    """
    Checks if a list of tokens are all non-empty.
    """
    return all(bool(token) for token in tokens)
