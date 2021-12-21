import pytest
from datetime import datetime


import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import src.misc as misc


def test_is_birthday():
    birthday_mama = datetime(year=2021, month=3, day=9)
    assert(misc.is_birthday(birthday_mama) == True)

    birthday_mama = datetime(year=1961, month=3, day=9)
    assert(misc.is_birthday(birthday_mama) == True)

    birthday_papa = datetime(year=2021, month=9, day=25)
    assert(misc.is_birthday(birthday_papa) == True)

    assert(misc.is_birthday(datetime(year=2021, month=1, day=1)) == False)


if __name__ == "__main__":
    test_is_birthday()
