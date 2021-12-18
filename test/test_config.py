import pytest

import os,sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__))) 


import src.config as cfg


def test_config():
    # Paths
    assert os.path.exists(cfg.DIR_PROJ_ROOT)
    assert os.path.exists(cfg.DIR_SRC)
    assert os.path.exists(cfg.DIR_RES)

    # Files
    assert os.path.exists(cfg.FILE_API_KEY)
    