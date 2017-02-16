import socket
import math

TCP_IP = '127.0.0.1'
TCP_PORT = 9003
BUFFER_SIZE = 1024
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
    snew = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if data[1] == '+':
        snew.connect((TCP_IP, 9004))
        snew.send(data)
        dato = snew.recv(BUFFER_SIZE)
        snew.close()
    if data[1] == '-':
        snew.connect((TCP_IP, 9005))
        snew.send(data)
        dato = snew.recv(BUFFER_SIZE)
        snew.close()
    if data[1] == '*':
        snew.connect((TCP_IP, 9006))
        snew.send(data)
        dato = snew.recv(BUFFER_SIZE)
        snew.close()
    if data[1] == '/':
        snew.connect((TCP_IP, 9007))
        snew.send(data)
        dato = snew.recv(BUFFER_SIZE)
        snew.close()
    if data[1] == '^':
        snew.connect((TCP_IP, 9008))
        snew.send(data)
        dato = snew.recv(BUFFER_SIZE)
        snew.close()
    if data[1] == 'r':
        snew.connect((TCP_IP, 9009))
        snew.send(data)
        dato = snew.recv(BUFFER_SIZE)
        snew.close()
    if data[1] == 'l':
        snew.connect((TCP_IP, 9010))
        snew.send(data)
        dato = snew.recv(BUFFER_SIZE)
        snew.close()
    if data == 'parar':
        dato = snew.recv(BUFFER_SIZE)
        conn.send("3")
        break
    clientes += 1
    conn.send(dato)
conn.close()
