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
        # Buffer size for receiving data
        self.recv_buffsize = 1024
        # The camera needs every command sent to it to be numbered
        self.command_number = 0

    def _getCommandNumber(self):
        self.command_number += 1
        return self.command_number

    def _send_to_cam(self, hex_command):
        command_type = bytearray.fromhex('01 00')
        command_body = bytearray.fromhex(hex_command)
        command_length = len(command_body).to_bytes(2, 'big')
        command_number = self._getCommandNumber().to_bytes(4, 'big')
        command = command_type + command_length + command_number + command_body
        self.connection.sendto(command, (self.ip, self.port))
        try:
            response = self.connection.recvfrom(self.recv_buffsize)
        except TimeoutError:
            raise TimeoutError("Camera took too long to respond")
        return binascii.hexlify(response[0])

    def powerOn(self):
        hex_command = "81 01 04 00 02 FF"
        return self._send_to_cam(hex_command)

    def powerOff(self):
        hex_command = "81 01 04 00 03 FF"
        return self._send_to_cam(hex_command)

    def zoomStop(self):
        hex_command = "81 01 04 07 00 FF"
        return self._send_to_cam(hex_command)

    def zoomIn(self, speed = None):
        if speed is None:
            hex_command = "81 01 04 07 02 FF"
            return self._send_to_cam(hex_command)
        else:
            if (0 <= speed <= 7):
                hex_command = f"81 01 04 07 2{speed} FF"
                return self._send_to_cam(hex_command)
            else:
                raise ZoomSpeedError

    def zoomOut(self, speed = None):
        if speed is None:
            hex_command = "81 01 04 07 03 FF"
            return self._send_to_cam(hex_command)
        else:
            if (0 <= speed <= 7):
                hex_command = f"81 01 04 07 3{speed} FF"
                return self._send_to_cam(hex_command)
            else:
                raise ZoomSpeedError
    
    def zoomSet(self, position):
        if (0 <= position <= 16384):
            # The '[2:]' removes '0x' from the beginning of the hex string
            hex_position = hex(position)[2:]
            s = hex_position[len(hex_position) - 1]
            r = hex_position[len(hex_position) - 2] or "0"
            q = hex_position[len(hex_position) - 3] or "0"
            p = hex_position[len(hex_position) - 4] or "0"
            hex_command = f"81 01 04 47 0{p} 0{q} 0{r} 0{s} FF"
            return self._send_to_cam(hex_command)
        else:
            raise ZoomPositionError
    
    def moveStop(self):
        hex_command = "81 01 06 01 00 00 03 03 FF"
        return self._send_to_cam(hex_command)
    
    def moveUp(self, speed):
        if (1 <= speed <= 17):
            hex_speed = hex(speed)[2:]
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 03 01 FF"
            return self._send_to_cam(hex_command)
        else:
            raise MoveSpeedError

    def moveDown(self, speed):
        if (1 <= speed <= 17):
            hex_speed = hex(speed)[2:]
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 03 02 FF"
            return self._send_to_cam(hex_command)
        else:
            raise MoveSpeedError

    def moveLeft(self, speed):
        if (1 <= speed <= 17):
            hex_speed = hex(speed)[2:]
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 01 03 FF"
            return self._send_to_cam(hex_command)
        else:
            raise MoveSpeedError

    def moveRight(self, speed):
        if (1 <= speed <= 17):
            hex_speed = hex(speed)[2:]
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 02 03 FF"
            return self._send_to_cam(hex_command)
        else:
            raise MoveSpeedError

    def moveUpLeft(self, speed):
        if (1 <= speed <= 17):
            hex_speed = hex(speed)[2:]
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 01 01 FF"
            return self._send_to_cam(hex_command)
        else:
            raise MoveSpeedError

    def moveUpRight(self, speed):
        if (1 <= speed <= 17):
            hex_speed = hex(speed)[2:]
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 02 01 FF"
            return self._send_to_cam(hex_command)
        else:
            raise MoveSpeedError

    def moveDownLeft(self, speed):
        if (1 <= speed <= 17):
            hex_speed = hex(speed)[2:]
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 02 01 FF"
            return self._send_to_cam(hex_command)
        else:
            raise MoveSpeedError

    def moveDownRight(self, speed):
        if (1 <= speed <= 17):
            hex_speed = hex(speed)[2:]
            hex_command = f"81 01 06 01 {hex_speed} {hex_speed} 02 02 FF"
            return self._send_to_cam(hex_command)
        else:
            raise MoveSpeedError
    
    def moveToCenter(self):
        hex_command = "81 01 06 04 FF"
        return self._send_to_cam(hex_command)