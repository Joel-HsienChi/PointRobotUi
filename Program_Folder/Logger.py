'''
This class is a simple logging class that provides easier logging experience. 
To use this loggin class, just create a logger object with desired parameter. 
For instance, to create a logger named: TestLogger with a level of INFO and located at "Log_Folder/Test.log",

You will have to declare a variable like following:

    TestLogger = logger_class("test_logger", logging.INFO, "Log_Folder/Test.log")

Then, to log the message into log file, call the created logger with .logger, then you will be able to log the 
message with desired level.

For instance to log a message into log file at info level, you will have to do it like:

    TestLogger.logger.info("This is a test info message )
'''
import logging


class logger_class:
    def __init__(self, logger_name, level, path):
        self.logger_name = logger_name
        self.level = level
        self.path = path

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s %(message)s")
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(self.level)
        handler = logging.FileHandler(self.path)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
