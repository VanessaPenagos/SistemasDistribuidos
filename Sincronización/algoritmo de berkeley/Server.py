import socket
import time

Mensaje = "Dame tu hora"

def UTCtoSeconds(hour):
	H, M, S = hour.split(":")
	Seconds  = ( (int(M) * 60) + (int(H) * 3600) + int(S) )
	return Seconds

def SecondstoUTC(seconds):
	H = seconds/3600
	M = (seconds - H*3600) /60
	S = seconds - H*3600 - M*60;
	Hora = str(H)+":"+str(M)+":"+str(S)
	return Hora

PORTS=[9001,9002,9003]
print "Esperando conexion"

while True:
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hora3=0

    s1.bind(('localhost', PORTS[0]))
    s1.listen(1)
    conexion1, clienteDireccion1 = s1.accept()
    conexion1.send(Mensaje)
    hora1=UTCtoSeconds(conexion1.recv(1024))

    s2.bind(('localhost', PORTS[1]))
    s2.listen(1)
    conexion2, clienteDireccion1 = s2.accept()
    conexion2.send(Mensaje)
    hora2=UTCtoSeconds(conexion2.recv(1024))

    s3.bind(('localhost', PORTS[2]))
    s3.listen(1)
    conexion3, clienteDireccion1 = s3.accept()
    conexion3.send(Mensaje)
    hora3=UTCtoSeconds(conexion3.recv(1024))

    prom= str(SecondstoUTC((hora1+hora2+hora3)/3))
    print prom
    conexion1.send(prom)
    conexion2.send(prom)
    conexion3.send(prom)

    conexion1.close()
    conexion2.close()
    conexion3.close()


