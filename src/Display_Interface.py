import sys
import os
import time
import traceback
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import colors
import pandas as pd

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

def generate_plot(data, outFileName):
    df = data.copy()
    df = df / 1000 # set to KWh
    df = df.iloc[1: , :]    # Drop first row

    # Plot lines
    scaling = 100
    fontsize = 14
    width = EPD_WIDTH / scaling
    height = EPD_HEIGHT / scaling
    cmap = colors.ListedColormap(["black"])

    # Add total consumption
    hours = pd.Timedelta(data.index.values[-1] - data.index.values[0]) / pd.Timedelta("1 hour")
    total_production = df["Production"].sum() / hours
    total_consumption = df["Consumption"].sum() / hours
    total = (total_consumption - total_production) 

    df.plot(style=["--", "-"], figsize=(width, height), cmap=cmap, fontsize=fontsize)

    # Formatting
    plt.title(f"Gesamtverbrauch (24h): {total:.2f}kWh", fontsize=fontsize*1.2)
    plt.grid(linewidth=2)
    plt.xlabel("")
    plt.ylabel("Leistung [kW]", fontsize=fontsize)
    plt.legend(labels=[f"Produktion: {total_production:.2f} kWh", f"Verbrauch:  {total_consumption:.2f} kWh"], fontsize=fontsize)
    plt.gca().xaxis.set_tick_params(which='both', width=3)
    plt.gca().yaxis.set_tick_params(which='both', width=3)


    # Output
    page_margin = 0.075
    plt.subplots_adjust(left=0.06, right=0.995, top=0.995, bottom=0.1)
    plt.savefig(outFileName, dpi=500, facecolor="white")



def display_image(fileName):
    epd = EPD()
    epd.init()

    # load image
    img = Image.open(fileName)

    # transform to binary array
    thresh =  cfg.BW_THRESH
    fn = lambda x : 255 if x > thresh else 0
    r = img.convert('L').point(fn, mode='1')

    # resize to fit display
    img = img.resize((cfg.EPD_WIDTH, cfg.EPD_HEIGHT))

    # write to display
    epd.display(epd.getbuffer(img))

    # save output to file as well
    file_out = cfg.DIR_OUT + "plot.bmp"
    img.save(file_out)



if __name__ == "__main__":
    display_image(cfg.DIR_OUT + "plot.png")