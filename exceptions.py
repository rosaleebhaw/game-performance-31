class GameError(Exception):
    """Base class for other exceptions in the game."""
    pass

class InvalidInputError(GameError):
    """Exception raised for invalid user inputs."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NotFoundError(GameError):
    """Exception raised when a required resource is not found."""
    def __init__(self, resource):
        self.resource = resource
        self.message = f'{resource} not found.'
        super().__init__(self.message)

class PermissionDeniedError(GameError):
    """Exception raised for permission-related issues."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

