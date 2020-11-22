from .viscaexceptions import *
import socket
import binascii

class Controller:
    def __init__(self, ip, port = 52381):
        self.ip = ip
        self.port = port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Timeout when receiving data
        self.connection.settimeout(2.0)
        # The camera needs every command sent to it to be numbered
        self.command_number = 0

    def _getCommandNumber(self):
        self.command_number += 1
        return self.command_number

    def _sendToCam(self, hex_command):
        command_type = bytearray.fromhex('01 00')
        command_body = bytearray.fromhex(hex_command)
        command_length = len(command_body).to_bytes(2, 'big')
        command_number = self._getCommandNumber().to_bytes(4, 'big')
        command = command_type + command_length + command_number + command_body
        self.connection.sendto(command, (self.ip, self.port))
        try:
            # 1024 is the buffer size for receiving data
            response = self.connection.recvfrom(1024)
        except socket.timeout:
            raise TimeoutError("Camera took too long to respond")
        return binascii.hexlify(response[0]).hex()

    def _intToHex(self, number):
        return number.to_bytes(2, byteorder='big', signed=True).hex()

    def _zoomPositionValid(self, position):
        if (0 <= position <= 16384):
            return True
        else:
            raise ZoomPositionError

    def _zoomSpeedValid(self, speed):
        if (0 <= speed <= 7):
            return True
        else:
            raise ZoomSpeedError

    def _moveSpeedValid(self, speed):
        if (1 <= speed <= 17):
            return True
        else:
            raise MoveSpeedError

    def _panPosValid(self, pos):
        if (-7707 <= pos <= 7707):
            return True
        else:
            raise PanPosError

    def _tiltPosValid(self, pos):
        if (-4080 <= pos <= 4080):
            return True
        else:
            raise TiltPosError

    def powerOn(self):
        hex_command = "81 01 04 00 02 FF"
        return self._sendToCam(hex_command)

    def powerOff(self):
        hex_command = "81 01 04 00 03 FF"
        return self._sendToCam(hex_command)

    def zoomStop(self):
        hex_command = "81 01 04 07 00 FF"
        return self._sendToCam(hex_command)

    def zoomIn(self, speed = None):
        if speed is None:
            hex_command = "81 01 04 07 02 FF"
            return self._sendToCam(hex_command)
        else:
            if (self._zoomSpeedValid(speed)):
                hex_command = f"81 01 04 07 2{speed} FF"
                return self._sendToCam(hex_command)

    def zoomOut(self, speed = None):
        if speed is None:
            hex_command = "81 01 04 07 03 FF"
            return self._sendToCam(hex_command)
        else:
            if (self._zoomSpeedValid(speed)):
                hex_command = f"81 01 04 07 3{speed} FF"
                return self._sendToCam(hex_command)
    
    def zoomSet(self, position):
        if (self._zoomPositionValid(position)):
            hex_pos = self._intToHex(position)
            hex_command = f"81 01 04 47 0{hex_pos[0]} 0{hex_pos[1]} 0{hex_pos[2]} 0{hex_pos[3]} FF"
            return self._sendToCam(hex_command)
    
    def moveStop(self):
        hex_command = "81 01 06 01 00 00 03 03 FF"
        return self._sendToCam(hex_command)
    
    def moveUp(self, speed):
        if (self._moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 03 01 FF"
            return self._sendToCam(hex_command)

    def moveDown(self, speed):
        if (self._moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 03 02 FF"
            return self._sendToCam(hex_command)

    def moveLeft(self, speed):
        if (self._moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 01 03 FF"
            return self._sendToCam(hex_command)

    def moveRight(self, speed):
        if (self._moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 02 03 FF"
            return self._sendToCam(hex_command)

    def moveUpLeft(self, speed):
        if (self._moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 01 01 FF"
            return self._sendToCam(hex_command)

    def moveUpRight(self, speed):
        if (self._moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 02 01 FF"
            return self._sendToCam(hex_command)

    def moveDownLeft(self, speed):
        if (self._moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 02 01 FF"
            return self._sendToCam(hex_command)

    def moveDownRight(self, speed):
        if (self._moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 02 02 FF"
            return self._sendToCam(hex_command)
    
    def moveToCenter(self):
        hex_command = "81 01 06 04 FF"
        return self._sendToCam(hex_command)

    def moveToAbsolute(self, speed, pan_pos, tilt_pos):
        if (self._moveSpeedValid(speed) and
        self._panPosValid(pan_pos) and
        self._tiltPosValid(tilt_pos)):
            hex_speed = self._intToHex(speed)
            hex_pan_pos = self._intToHex(pan_pos)
            hex_tilt_pos = self._intToHex(tilt_pos)
            hex_command = f"81 01 06 02 "
            f"{hex_speed} {hex_speed} "
            f"0{hex_pan_pos[0]} 0{hex_pan_pos[1]} 0{hex_pan_pos[2]} 0{hex_pan_pos[3]} "
            f"0{hex_tilt_pos[0]} 0{hex_tilt_pos[1]} 0{hex_tilt_pos[2]} 0{hex_tilt_pos[3]} FF"
            return self._sendToCam(hex_command)
