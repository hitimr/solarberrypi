import platform

def is_raspi():
    if(platform.machine() == "armv7l"): return True
    return False
