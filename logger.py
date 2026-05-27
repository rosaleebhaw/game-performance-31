import logging

# Configure the logger to output messages to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GameLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

# Sample usage to demonstrate functionality
if __name__ == '__main__':
    logger = GameLogger('GamePerformance')
    logger.info('Game started successfully!')
    logger.debug('Loading assets...')
    logger.warning('Low memory warning!')
    logger.error('An error occurred!')
    logger.critical('Critical failure! Ending game...')
