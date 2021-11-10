#Usar python 2
#CLIENTE
import socket

HOST = '127.0.0.1' #esse é o local host é o endereço da sua própria máquina.
PORT = 5000 #definir uma porta


#aqui você escolhe se vai usar TCP ou UDP
#vamos usar o UDP
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dest = (HOST,PORT) #onde você vai mandar.
print 'Para sair use CTRL+X\n'
msg = raw_input() # a linha que vai receber a nossa mensagem
while msg <> '\x18':
    udp.sendto(msg,dest)
    msg = raw_input()

udp.close

