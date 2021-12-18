import pytest
import pandas as pd
import shutil
from datetime import datetime, timedelta

import os,sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__))) 

import src.config as cfg
import src.misc as misc
from src.SE_Interface import SE_Interface
from src.Display_Interface import generate_plot, display_image


# remove old test output
if os.path.exists(cfg.DIR_OUT_TEST):
    shutil.rmtree(cfg.DIR_OUT_TEST)
os.makedirs(cfg.DIR_OUT_TEST, exist_ok=True)


def test_SE_Interface():
    se_interface = SE_Interface()

    now = datetime.now()
    #now = datetime(year=2021, month=8, day=15, hour=23)
    se_interface.request_SitePowerDetailed(now, timedelta(days=1), safeToFile=True)

    assert(len(se_interface.data) > 0)


def test_generate_plot():
    # read prepared data, generate a plot and check if a file was written
    df = pd.read_csv("test/res/test_data.csv")

    outFile = cfg.DIR_OUT_TEST + "plot.png"
    generate_plot(df, outFile)   
    assert(os.path.isfile(outFile))   


@pytest.mark.skipif(misc.is_raspi() == False, reason="RaspberryPi required")
def test_display_image():
    display_image(cfg.DIR_OUT_TEST + "plot.png")





if __name__ == "__main__":
    #test_SE_Interface()
    #test_generate_plot()
    pass