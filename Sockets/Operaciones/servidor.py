import socket
import math



TCP_IP = '127.0.0.1'
TCP_PORT = 9003
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
    Dato1, Dato2 = data.split(" ")
    suma = int(Dato1) + int(Dato2)
    resta = int(Dato1) - int(Dato2)
    multiplicacion = int(Dato1) * int(Dato2)
    potencia = pow(int(Dato1), int(Dato2))
    #Validacion
    #Division
    if Dato2 == '0':
        division='Error'
    else:
        division = int(Dato1) / int(Dato2)

    #raiz
    if Dato2 == '0' or Dato1 < 0:
        raiz = "Error"
    else :
        raiz = pow( int(Dato1) , (1 / int(Dato2)))


    conn.send( str(suma)+","+str(resta)+","+str(multiplicacion)+","+str(division)+","+str(potencia)+","+str(raiz))
    if clientes == 2:
        conn.send("3")
        break
    clientes+=1

conn.close()
