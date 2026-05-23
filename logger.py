import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=3):
    """
    Set up a logger with rotating file handler.
    
    Args:
        log_file (str): Name of the log file.
        max_bytes (int): Maximum file size before rotation.
        backup_count (int): Number of backup files to keep.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Example usage:
if __name__ == '__main__':
    logger = setup_logger()
    logger.debug('This is a debug message.')
    logger.info('Informational message for the log.')
    logger.warning('Warning: something might be wrong!')
    logger.error('An error occurred!')
    logger.critical('Critical issue present!')
