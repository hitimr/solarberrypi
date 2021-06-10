import pytest
import os
import sys
from pathlib import Path

# Add parent folder to search path
sys.argv.insert(0, Path(__file__).parent.parent.absolute())


import src.config as cfg


def test_config():
    assert os.path.exists(cfg.DIR_PROJ_ROOT)
    assert os.path.exists(cfg.DIR_SRC)
    assert os.path.exists(cfg.DIR_RES)