#Usar python 2
#SERVIDOR
import socket
HOST = ''
PORT = 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
while True:
    msg, client = udp.recvfrom(1024)
    print client, msg
udp.close
