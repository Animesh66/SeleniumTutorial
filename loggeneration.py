import logging


logging.basicConfig(filename="/Users/animeshmukherjee/Desktop/Animesh/Log_file/newfile.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',  # this is to format the log
                    datefmt='%m/%d/%Y %I:%M:%S  %p',  # this is to format time
                    level=logging.DEBUG
                    )  # this will create a logfile in the specified folder
logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is am error message")
logging.critical("This is a critical message")
