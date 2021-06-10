import sys
import os
from pathlib import Path

# Add parent folder to search path
sys.argv.insert(0,Path(__file__).parent.parent.absolute())

# Platform specific separators
if os.name == 'nt': SEP = "\\"  # Windows
else: SEP = "/" # Linux


DIR_PROJ_ROOT = str(Path(__file__).parent.parent.absolute()) + SEP
DIR_SRC = Path(DIR_PROJ_ROOT + "src" + SEP)
DIR_RES = Path(DIR_PROJ_ROOT + "res" + SEP)
