class ZoomSpeedError(BaseException):
    def __init__(self):
        self.message = "Zoom speed must be between 0 and 7"
        super().__init__(self.message)

class ZoomPositionError(BaseException):
    def __init__(self):
        self.message = "Zoom position must be between 0 and 16384"
        super().__init__(self.message)

class MoveSpeedError(BaseException):
    def __init__(self):
        self.message = "Move speed must be between 1 and 17"
        super().__init__(self.message)

class PanPosError(BaseException):
    def __init__(self):
        self.message = "Pan position must be between -1660 and 1660"
        super().__init__(self.message)

class TiltPosError(BaseException):
    def __init__(self):
        self.message = "Tilt position must be between -374 and 1122"
        super().__init__(self.message)
