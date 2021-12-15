import sys
import os
from pathlib import Path

# Add parent folder to search path
sys.argv.insert(0,Path(__file__).parent.parent.absolute())

# Platform specific separators
if os.name == 'nt': SEP = "\\"  # Windows
else: SEP = "/" # Linux

# Paths
DIR_PROJ_ROOT = str(Path(__file__).parent.parent.absolute()) + SEP
DIR_SRC = DIR_PROJ_ROOT + "src" + SEP
DIR_RES = DIR_PROJ_ROOT + "res" + SEP

# Files
FILE_API_KEY = DIR_RES + "api_key.csv"

# SolarEdge
SITE_ID = "2130766"

# URLs
URL_SOLAR_EDGE_JSON_ENDPOINT = "https://monitoringapi.solaredge.com/sites/list?size=5&searchText=Lyon&sortProperty=name&sortOrder=ASC&api_key="
URL_SOLAR_EDGE_BASE = "https://monitoringapi.solaredge.com/site/" + str(SITE_ID) + "/"


# Dispaly Settings
EPD_WIDTH       = 800
EPD_HEIGHT      = 480
EPD_DPI         = 122


# Misc
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
STATUS_CODE_OK = 200