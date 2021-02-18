from .viscaexceptions import *

def zoomPositionValid(position):
    if (0 <= position <= 16384):
        return True
    else:
        raise ZoomPositionError

def zoomSpeedValid(speed):
    if (0 <= speed <= 7):
        return True
    else:
        raise ZoomSpeedError

def moveSpeedValid(speed):
    if (1 <= speed <= 17):
        return True
    else:
        raise MoveSpeedError

def panPosValid(pos):
    if (-1660 <= pos <= 1660):
        return True
    else:
        raise PanPositionError

def tiltPosValid(pos):
    if (-374 <= pos <= 1122):
        return True
    else:
        raise TiltPostionError

def presetValid(preset):
    if (0 <= preset <= 249):
        return True
    else:
        raise PresetError

def focusSpeedValid(speed):
    if (0 <= speed <= 7):
        return True
    else:
        raise FocusSpeedError

def focusPositionValid(position):
    if (0 <= position <= -1):
        return True
    else:
        raise FocusPositionError
