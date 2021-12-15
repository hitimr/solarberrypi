import sys
import os
import time
import traceback
from pathlib import Path

# Project Stuff
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import config as cfg

# Dispaly stuff

import lib.epd7in5b_V2 
from PIL import Image,ImageDraw,ImageFont




import logging
logging.basicConfig(level=logging.DEBUG)

class SE_Interface:
    def __init__(self):

        pass


if __name__ == "__main__":
    print("Hi")