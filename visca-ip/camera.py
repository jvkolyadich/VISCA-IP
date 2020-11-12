import socket
class Camera:
    def __init__(self, ip, port=52381):
        self.ip = ip
        self.port = port

    def init_connection(self):
        
