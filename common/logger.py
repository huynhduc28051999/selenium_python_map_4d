import logging
import os
import time

class Log(object):
    """Write a log class for other modules to call"""
    def __init__(self, logger):
        # The concatenated log folder, if it does not exist, it will be created automatically
        cur_path = os.path.dirname(os.path.realpath(__file__))
        log_path = os.path.join(os.path.dirname(cur_path), 'logs')
        if not os.path.exists(log_path):os.mkdir(log_path)

        # Set the log file name format and log level
        self.log_name = os.path.join(log_path, '%s.log' % time.strftime('%Y-%m-%d'))
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # Create a handler that writes logs to a log file
        fh = logging.FileHandler(self.log_name, 'a' ,encoding='utf-8')
        fh.setLevel(logging.INFO)

        # Create another handler to output the log to the console
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # Define the log output format
        self.formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
        ch.setFormatter(self.formatter)
        fh.setFormatter(self.formatter)

        # Add handler to logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def get_log(self):
        return self.logger

