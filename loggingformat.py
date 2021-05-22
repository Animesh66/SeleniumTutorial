import logging


logging.basicConfig(filename="/Users/animeshmukherjee/Desktop/Animesh/Log_file/loggerfile.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',  # this is to format the log
                    datefmt='%m/%d/%Y %I:%M:%S  %p',  # this is to format time
                    )  # this will create a logfile in the specified folder
logger = logging.getLogger() # create a new logger object
logger.setLevel(logging.DEBUG)
logger.debug("This is a debug message")
logger.info("This is a info message")
logger.warning("This is a warning message")
logger.error("This is am error message")
logger.critical("This is a critical message")
