from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import random
import time
import threading
import os

IP = '127.0.0.1'
PUERTO = 8008
Archivos = ["hola.txt", "vane.txt", "diego.txt"]

#################### SERVIDOR ###########################

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer((IP,PUERTO),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
	def LeerArchivo(self, nombrearchivo):
		archivo = open(nombrearchivo,"r")
		contenido = archivo.read()
		archivo.close()
		return contenido

	def ModificarArchivos(self, nombrearchivo):
		os.popen("notepad "+nombrearchivo)

server.register_instance(MyFuncs())

t = threading.Thread(target=server.serve_forever)
t.start()

##################### CLIENTE ###########################

server = xmlrpclib.ServerProxy('http://localhost:8006')
registroCliente = server.RegistrarCliente(IP, PUERTO)
if registroCliente != "Cliente ya registrado":
	for i in Archivos:
		registroArchivo = server.RegistrarArchivos(i, IP, PUERTO)
		time.sleep(1)

while True:
	print "\n 1. Listar archivos \n 2. Buscar Archivo"
	opcion = raw_input("Elija una opcion: ")
	if opcion == '1':
		archivos = server.ListarArchivos()
		i = 1
		print "Los archivos disponibles son: "
		for elemento in archivos:
			print str(i) + ". " + elemento
			i += 1
	if opcion == '2':
		nombre = raw_input("Ingrese el nombre del archivo(con su extension): ")
		direccion = server.BuscarArchivo(nombre)
		if direccion == "Nope":
			print "No se encuentra el archivo"
		else:
			maquinaN = xmlrpclib.ServerProxy(direccion)
			contenido = maquinaN.LeerArchivo(nombre)
			print "\n",contenido
			maquinaN.ModificarArchivos(nombre)
			


 
