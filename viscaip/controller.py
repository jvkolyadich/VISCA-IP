from .validation import *
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
        '''
        try:
            # 1024 is the buffer size for receiving data
            response = self.connection.recvfrom(1024)
            return binascii.hexlify(response[0]).hex()
        except socket.timeout:
            return None
        '''
        return None

    def _intToHex(self, number, size = 1):
        return number.to_bytes(size, byteorder='big', signed=True).hex()

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
            if (zoomSpeedValid(speed)):
                hex_command = f"81 01 04 07 2{speed} FF"
                return self._sendToCam(hex_command)

    def zoomOut(self, speed = None):
        if speed is None:
            hex_command = "81 01 04 07 03 FF"
            return self._sendToCam(hex_command)
        else:
            if (zoomSpeedValid(speed)):
                hex_command = f"81 01 04 07 3{speed} FF"
                return self._sendToCam(hex_command)

    def zoomSet(self, position):
        if (zoomPositionValid(position)):
            hex_pos = self._intToHex(position, 2)
            hex_command = f"81 01 04 47 0{hex_pos[0]} 0{hex_pos[1]} 0{hex_pos[2]} 0{hex_pos[3]} FF"
            return self._sendToCam(hex_command)

    def moveStop(self):
        hex_command = "81 01 06 01 00 00 03 03 FF"
        return self._sendToCam(hex_command)

    def moveUp(self, speed):
        if (moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 03 01 FF"
            return self._sendToCam(hex_command)

    def moveDown(self, speed):
        if (moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 03 02 FF"
            return self._sendToCam(hex_command)

    def moveLeft(self, speed):
        if (moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 01 03 FF"
            return self._sendToCam(hex_command)

    def moveRight(self, speed):
        if (moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 02 03 FF"
            return self._sendToCam(hex_command)

    def moveUpLeft(self, speed):
        if (moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 01 01 FF"
            return self._sendToCam(hex_command)

    def moveUpRight(self, speed):
        if (moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 02 01 FF"
            return self._sendToCam(hex_command)

    def moveDownLeft(self, speed):
        if (moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 01 02 FF"
            return self._sendToCam(hex_command)

    def moveDownRight(self, speed):
        if (moveSpeedValid(speed)):
            hex_speed = self._intToHex(speed)
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 02 02 FF"
            return self._sendToCam(hex_command)

    def moveToCenter(self):
        hex_command = "81 01 06 04 FF"
        return self._sendToCam(hex_command)

    def moveToAbsolute(self, speed, pan_pos, tilt_pos):
        if (moveSpeedValid(speed) and
        panPosValid(pan_pos) and
        tiltPosValid(tilt_pos)):
            hex_speed = self._intToHex(speed)
            hex_pan_pos = self._intToHex(pan_pos, 2)
            hex_tilt_pos = self._intToHex(tilt_pos, 2)
            hex_command = f"81 01 06 02 {hex_speed} {hex_speed} 0{hex_pan_pos[0]} 0{hex_pan_pos[1]} 0{hex_pan_pos[2]} 0{hex_pan_pos[3]} 0{hex_tilt_pos[0]} 0{hex_tilt_pos[1]} 0{hex_tilt_pos[2]} 0{hex_tilt_pos[3]} FF"
            return self._sendToCam(hex_command)

    def presetReset(self, preset):
        if (presetValid(preset)):
            hex_preset = self._intToHex(preset)
            hex_command = f"81 01 04 3F 00 {hex_preset} FF"
            return self._sendToCam(hex_command)

    def presetSet(self, preset):
        if (presetValid(preset)):
            hex_preset = self._intToHex(preset)
            hex_command = f"81 01 04 3F 01 {hex_preset} FF"
            return self._sendToCam(hex_command)

    def presetRecall(self, preset):
        if (presetValid(preset)):
            hex_preset = self._intToHex(preset)
            hex_command = f"81 01 04 3F 02 {hex_preset} FF"
            return self._sendToCam(hex_command)

    def focusStop(self):
        hex_command = "81 01 04 08 00 FF"
        return self._sendToCam(hex_command)

    def focusFar(self, speed = None):
        if speed is None:
            hex_command = "81 01 04 08 02 FF"
            return self._sendToCam(hex_command)
        else:
            if (focusSpeedValid(speed)):
                hex_command = f"81 01 04 08 2{speed} FF"
                return self._sendToCam(hex_command)

    def focusNear(self, speed = None):
        if speed is None:
            hex_command = "81 01 04 08 03 FF"
            return self._sendToCam(hex_command)
        else:
            if (focusSpeedValid(speed)):
                hex_command = f"81 01 04 08 3{speed} FF"
                return self._sendToCam(hex_command)

    def focusSet(self, position):
        if (focusPositionValid(position)):
            hex_pos = self._intToHex(position, 2)
            hex_command = f"81 01 04 48 0{hex_pos[0]} 0{hex_pos[1]} 0{hex_pos[2]} 0{hex_pos[3]} FF"
            return self._sendToCam(hex_command)
