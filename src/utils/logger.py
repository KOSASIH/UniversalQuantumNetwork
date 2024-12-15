import logging

class Logger:
    def __init__(self, name='UQNLogger', level=logging.INFO):
        """Initialize the logger with a specified name and logging level."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.FileHandler('uqn.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_info(self, message):
        """Log an informational message."""
        self.logger.info(message)

    def log_warning(self, message):
        """Log a warning message."""
        self.logger.warning(message)

    def log_error(self, message):
        """Log an error message."""
        self.logger.error(message)

if __name__ == "__main__":
    logger = Logger()
    logger.log_info("Logger initialized.")
    logger.log_warning("This is a warning message.")
    logger.log_error("This is an error message.")
