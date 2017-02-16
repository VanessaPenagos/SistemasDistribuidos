import socket
import math

TCP_IP = '127.0.0.1'
TCP_PORT = 9004
BUFFER_SIZE = 20
suma = 0
Datos = []
clientes = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while 1:
    print "Esperando conexion"
    conn, addr = s.accept()
    data = conn.recv(BUFFER_SIZE)
    print data
    if data == 'parar':
        break
    Dato1, Dato2 = data.split("+")
    suma = int(Dato1) + int(Dato2)
    print "Suma: ", suma
    conn.send(str(suma))
conn.close()
