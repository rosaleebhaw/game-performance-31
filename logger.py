import logging
from logging.handlers import RotatingFileHandler
import os

class Logger:
    def __init__(self, name='game_logger', log_file='game.log', max_bytes=10*1024*1024, backup_count=5):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def get_logger(self):
        return self.logger

if __name__ == '__main__':
    log = Logger().get_logger()
    log.debug('Debugging message')
    log.info('Informational message')
    log.warning('Warning message')
    log.error('Error message')
    log.critical('Critical message')
