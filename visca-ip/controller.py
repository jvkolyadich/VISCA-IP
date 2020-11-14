import socket
import binascii

class Controller:
    def __init__(self, ip, port = 52381):
        self.ip = ip
        self.port = port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
            hex_command = f"81 01 04 07 2{speed} FF"
            return self._send_to_cam(hex_command)

    def zoomOut(self, speed = None):
        if speed is None:
            hex_command = "81 01 04 07 03 FF"
            return self._send_to_cam(hex_command)
        else:
            hex_command = f"81 01 04 07 3{speed} FF"
            return self._send_to_cam(hex_command)