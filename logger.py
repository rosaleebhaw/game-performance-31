import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file, max_bytes=5*1024*1024, backup_count=3):
    """
    Set up a logger with rotation.
    Args:
        log_file (str): The name of the log file.
        max_bytes (int): The maximum file size before rotation.
        backup_count (int): The number of backup files to keep.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

# Example usage
if __name__ == '__main__':
    logfile = 'game.log'
    logger = setup_logger(logfile)
    logger.info('Logger set up successfully.')