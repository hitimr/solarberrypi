import src.misc as misc
import src.config as cfg
import logging
import time
import traceback
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib import colors
import pandas as pd

# Project Stuff
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


# Dispaly stuff
if misc.is_raspi():
    from lib.epd7in5_V2 import *
    from PIL import Image, ImageDraw, ImageFont


def generate_plot(data, outFileName=""):
    if(len(data) == 0):
        raise ValueError("DataFrame seems to be empty")

    logging.info("Processing data")
    df = data.copy()
    df = df[["SelfConsumption", "Purchased", "FeedIn"]]
    df = df / 1000  # set to KWh
    df = df.iloc[1:, :]    # Drop first row

    # Plot lines
    scaling = 100
    fontsize = 14
    width = cfg.EPD_WIDTH / scaling
    height = cfg.EPD_HEIGHT / scaling
    cmap = colors.ListedColormap(["black"])

    # Add total consumption
    hours = float(
        (data.index.values[-1] - data.index.values[0])) * 10**-9 / (3600 * 4)
    total_selfConsumption = df["SelfConsumption"].sum() / hours
    total_purchased = df["Purchased"].sum() / hours
    total_feedin = df["FeedIn"].sum() / hours
    total = (total_purchased - total_selfConsumption - total_feedin)

    df.plot(
        style=["-", "--", ":"],
        figsize=(width, height),
        cmap=cmap,
        fontsize=fontsize,
        stacked=True
    )

    plt.fill_between(df.index, df["SelfConsumption"])

    # Formatting
    for line in plt.gca().get_lines():
        line.set_linewidth(2)  # Line thickness
    plt.title(
        f"Gesamtverbrauch (24h): {total:.2f}kWh", fontsize=fontsize * 1.2)
    plt.grid(linewidth=2)
    plt.xlabel("")
    plt.ylabel("Leistung [kW]", fontsize=fontsize * 1.2)
    plt.legend(
        labels=[
            f"Produktion: {total_selfConsumption:.2f} kWh",
            f"Zukauf:       {total_purchased:.2f} kWh",
            f"Rückspeis.: {total_feedin:.2f} kWh", ],
        fontsize=fontsize)
    plt.gca().xaxis.set_tick_params(which='both', width=3, labelsize=16)
    plt.gca().yaxis.set_tick_params(which='both', width=3, labelsize=16)
    plt.ylim([0, df.max().max() * 1.1])

    # Output
    # plt.tight_layout()
    page_margin = 0.075
    plt.subplots_adjust(left=0.07, right=0.995, top=0.995, bottom=0.11)
    plt.savefig("out/plot.png", dpi=500, facecolor="white")

    # Output
    if(outFileName != ""):
        logging.info("Exporting as .png")
        plt.savefig(outFileName, dpi=500, facecolor="white")


def display_image(fileName):
    if(misc.is_raspi() == False):
        raise NotImplementedError(
            "This machine probably has no interface installed")

    # load image
    logging.info("Transforming to binary bitmap")
    img = Image.open(fileName)

    # transform to binary array
    thresh = cfg.BW_THRESH
    def fn(x): return 255 if x > thresh else 0
    r = img.convert('L').point(fn, mode='1')

    # resize to fit display
    img = img.resize((cfg.EPD_WIDTH, cfg.EPD_HEIGHT))

    # write to display
    logging.info("Initializing Display")
    epd = EPD()
    epd.init()

    # save output to file as well
    logging.info("Saving bitmap")
    file_out = cfg.DIR_OUT + "plot.bmp"
    img.save(file_out)

    logging.info("Writing data")
    epd.display(epd.getbuffer(img))
    logging.info("Writing data complete")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    data = pd.read_csv(cfg.DIR_OUT + "last_data.csv")
    plotFile = cfg.DIR_OUT + "plot.png"
    generate_plot(data, plotFile)
