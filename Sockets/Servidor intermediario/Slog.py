import socket
import math

TCP_IP = '127.0.0.1'
TCP_PORT = 9010
BUFFER_SIZE = 20
Datos = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(3)

while 1:
    print "Esperando conexion"
    conn, addr = s.accept()
    data = conn.recv(BUFFER_SIZE)
    print data
    if data == 'parar':
        break
    print "Data: ", data
    Dato1, Dato2 = data.split("l")
    logaritmo = math.log(int(Dato1), int(Dato2))
    print logaritmo
    conn.send(str(logaritmo))
conn.close()
