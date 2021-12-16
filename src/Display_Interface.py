import sys
import os
import time
import traceback
from pathlib import Path
import numpy as np

# Project Stuff
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import logging
logging.basicConfig(level=logging.DEBUG)

import config as cfg

# Dispaly stuff
from lib.epd7in5_V2 import *
from PIL import Image,ImageDraw,ImageFont



class SE_Interface:
    def __init__(self):

        pass


if __name__ == "__main__":
    epd = EPD()

    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    Himage = Image.open("../out/plot.bmp")
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)
    print("Hi")