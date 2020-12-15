import socket
import binascii

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 52381
connection.bind(('', port))

while True:
    response = connection.recvfrom(1024)
    response = str(binascii.hexlify(response[0]))
    response = ' '.join(response[i:i+2] for i in range(2, len(response)-1, 2))
    print(response)
