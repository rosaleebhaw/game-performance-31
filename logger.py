import logging
from typing import Optional


def setup_logger(name: str, log_file: str, level: Optional[int] = logging.INFO) -> logging.Logger:
    """
    Sets up a logger with the specified name and log file.

    Args:
        name (str): The name of the logger.
        log_file (str): The file where logs will be stored.
        level (Optional[int]): The logging level (default is INFO).

    Returns:
        logging.Logger: The configured logger instance.
    """
    handler = logging.FileHandler(log_file)
    handler.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# Example usage
if __name__ == '__main__':
    logger = setup_logger('my_logger', 'my_log.log')
    logger.info('This is an info message')
    logger.error('This is an error message')
