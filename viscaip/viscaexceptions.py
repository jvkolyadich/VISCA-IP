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