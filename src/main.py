from datetime import date, datetime
import logging

from config import *
from SE_Interface import *
from Display_Interface import *
import misc


if __name__ == "__main__":
    now = datetime.now()
    se_interface = SE_Interface()
    data = se_interface.request_SitePowerDetailed(datetime.now(), timedelta(days=1))

    logging.info("Generating plot")
    plotFile = DIR_OUT + "plot.png"
    generate_plot(data, plotFile)

    if misc.is_raspi():
        logging.info("Displaying Image")
        display_image(plotFile)
        logging.info("Finished")
    else:
       logging.warning("No image is displayed because no Raspberry Pi is detected.") 

    


    

