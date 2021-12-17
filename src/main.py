from datetime import date, datetime
import logging
from logging.handlers import TimedRotatingFileHandler

from config import *
from SE_Interface import *
from Display_Interface import *
import misc


if __name__ == "__main__":
    # Init Logger
    now = datetime.now()
    se_interface = SE_Interface()
    data = se_interface.request_SitePowerDetailed(datetime.now(), timedelta(days=1))

    plotFile = DIR_OUT + "plot.png"
    generate_plot(data, plotFile)
    
    if misc.is_raspi():
        display_image(plotFile)


    

