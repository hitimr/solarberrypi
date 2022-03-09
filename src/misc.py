import platform


def is_raspi():
    if(platform.machine() == "armv7l"):
        return True
    return False


def is_birthday(date):
    # Mama
    if(date.month == 3 and date.day == 9):
        return True

    # 2022 she was on holiday on her birthday
    # she asked to extend by 1 day
    if((date.month == 3) and (date.day == 10) and (date.year == 2022)):
        return True

    # Papa
    if(date.month == 9 and date.day == 25):
        return True

    return False
