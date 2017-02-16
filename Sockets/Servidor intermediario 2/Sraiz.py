import socket
import math

TCP_IP = '127.0.0.1'
TCP_PORT = 9009
BUFFER_SIZE = 20
ndatos = 0
suma = 0
multp = 1
Datos = []
clientes = 0

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
    Dato1, Dato2 = data.split("r")
    #raiz
    if Dato2 == '0' or Dato1 < 0:
        raiz = "Error"
    else :
        raiz = pow( int(Dato1) , (1.0 / int(Dato2)))
        print "Raiz: ", raiz
    conn.send(str(raiz))

conn.close()
