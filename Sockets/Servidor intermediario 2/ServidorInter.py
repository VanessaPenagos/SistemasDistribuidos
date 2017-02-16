import socket
import math

TCP_IP = '127.0.0.1'
TCP_PORT = 9003
TCP_PORTS = ['9004','9005','9006','9007','9008','9009', '9010']
TPC_IPS = ['127.0.0.1','127.0.0.1','127.0.0.1','127.0.0.1','127.0.0.1','127.0.0.1',]
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(3)

while 1:
    print "Esperando conexion"
    conn, addr = s.accept()
    data = conn.recv(BUFFER_SIZE)
    if data[1] == '+':
    	servidor=TCP_PORTS[0]+'?'+TPC_IPS[0]
    	conn.send(servidor)
    if data[1] == '-':
    	servidor=TCP_PORTS[1]+'?'+TPC_IPS[1]
    	conn.send(servidor)
    if data[1] == '*':
        servidor=TCP_PORTS[2]+'?'+TPC_IPS[2]
    	conn.send(servidor)
    if data[1] == '/':
        servidor=TCP_PORTS[3]+'?'+TPC_IPS[3]
    	conn.send(servidor)
    if data[1] == '^':
        servidor=TCP_PORTS[4]+'?'+TPC_IPS[4]
    	conn.send(servidor)
    if data[1] == 'r':
        servidor=TCP_PORTS[5]+'?'+TPC_IPS[5]
    	conn.send(servidor)
    if data[1] == 'l':
        servidor=TCP_PORTS[5]+'?'+TPC_IPS[6]
    	conn.send(servidor)


    if data == 'parar':
        dato = snew.recv(BUFFER_SIZE)
        conn.send("3")
        break

conn.close()
