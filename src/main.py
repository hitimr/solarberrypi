from datetime import date, datetime
import logging
from logging.handlers import TimedRotatingFileHandler

from config import *
from SE_Interface import *


if __name__ == "__main__":
    # Init Logger
    now = datetime.now()
    logfilename = LOGGING_BASE_FILENAME + "_" + now.strftime("%y%m%d")
    logging.basicConfig(filename=LOGGING_BASE_FILENAME, filemode="a", encoding='utf-8', level=logging.DEBUG)

    logging.info("Initialising SE Interface")
    se_interface = SE_Interface()


    #data = se_interface.request_SitePowerDetailed(datetime.now(), timedelta(days=1))
    #assert

