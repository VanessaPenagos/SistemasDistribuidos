import xmlrpclib
import random
import time


##################### CLIENTE ###########################

IP = '127.0.0.1'
PUERTO = 8007
Archivos = ["hola.txt", "vane.txt", "diego.txt"]

server = xmlrpclib.ServerProxy('http://localhost:8006')
registroCliente = server.RegistrarCliente(IP, PUERTO)
print registroCliente
if registroCliente != "Cliente ya registrado":
	for i in Archivos:
		registroArchivo = server.RegistrarArchivos(i, IP, PUERTO)
		time.sleep(1)
		print registroArchivo