import logging
import os

class Logger:
    """Class for logging events and errors."""
    
    def __init__(self, log_file='app.log'):
        self.log_file = log_file
        self.setup_logger()

    def setup_logger(self):
        """Set up the logger with specified format and level."""
        logging.basicConfig(
            filename=self.log_file,
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        print(f"Logging is set up. Logs will be written to '{self.log_file}'.")

    def log_info(self, message):
        """Log an informational message."""
        logging.info(message)

    def log_warning(self, message):
        """Log a warning message."""
        logging.warning(message)

    def log_error(self, message):
        """Log an error message."""
        logging.error(message)

    def log_debug(self, message):
        """Log a debug message."""
        logging.debug(message)

# Example usage
if __name__ == "__main__":
    logger = Logger()
    logger.log_info("Application started.")
    logger.log_warning("This is a warning message.")
    logger.log_error("An error occurred.")
    logger.log_debug("Debugging information.")
