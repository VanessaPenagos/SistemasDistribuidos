import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 9003
BUFFER_SIZE = 1024

print "Digite dos numeros separados por un espacio"
Numero1=raw_input()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(Numero1)
data = s.recv(BUFFER_SIZE)
s.close()

if data!="3":
	suma, resta, multp, div, pot, raiz = data.split(",")
	print "La suma es:", suma
	print "La resta es:", resta
	print "La multiplicacion es:", multp
	print "La division es:", div
	print "La potencia es:", pot
	print "La raiz es:", raiz
