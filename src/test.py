import sys
from datetime import date, datetime, timedelta
sys.path.insert(0, ".")
from SE_Interface import *
import config as cfg


se_interface = SE_Interface()

now = datetime(year=2021, month=8, day=15, hour=23)
se_interface.request_SitePowerDetailed(now, timedelta(days=2))