from datetime import date, datetime
import logging

from matplotlib.pyplot import plot

from config import *
from SE_Interface import *
from Display_Interface import *
import misc


if __name__ == "__main__":
    #now = datetime(year=2021, month=8, day=10, hour=23)
    now = datetime.now()

    if(misc.is_birthday(now) == False):
        se_interface = SE_Interface()
        data = se_interface.request_SitePowerDetailed(
            now, timedelta(days=1))

        logging.info("Generating plot")
        plotFile = DIR_OUT + "plot.png"
        generate_plot(data, plotFile)

    else:
        logging.info("Birthday detected")
        plotFile = BIRTHDAY_IMAGE

    if misc.is_raspi():
        logging.info("Displaying Image")
        display_image(plotFile)
        logging.info("Finished")
    else:
        logging.warning(
            "No image is displayed because no Raspberry Pi is detected.")
