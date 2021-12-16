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
import pandas
from lib.epd7in5_V2 import *
from PIL import Image,ImageDraw,ImageFont



class Display_Interface:
    self.width = int
    self.height = int

    def __init__(self, width=cfg.EPD_WIDTH, height=cfg.EPD_HEIGHT):
        # class init
        self.width = int(width)
        self.heigth = int(height)

        # Init hardware
        self.epd = EPD()
        self.epd.init()
        self.epd.Clear()
    
    def display_image(self, fileName):
        # load image
        img = Image.open(fileName)

        # transform to binary array
        thresh =  cfg.BW_THRESH
        fn = lambda x : 255 if x > thresh else 0
        r = img.convert('L').point(fn, mode='1')

        # resize to fit display
        img = img.resize((self.width, self.height))
        #file_out = DIR_OUT + "plot.bmp"
        #img.save(file_out)

        Himage = Image.open(img)
        self.epd.display(epd.getbuffer(Himage))
        time.sleep(1)


if __name__ == "__main__":
    di = Display_Interface()
    di.display_image("../out/plot.png")