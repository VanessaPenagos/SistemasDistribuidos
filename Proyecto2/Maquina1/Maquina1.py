from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import random
import time
import threading
import os

IP = '127.0.0.1'
PUERTO = 8004
MisPaginas = ["M1P1.txt", "M1P2.txt", "M1P3.txt"]
PaginasDisponibles = ["M1P1.txt", "M1P2.txt", "M1P3.txt"]
Capacidad = [10, 8, 5]

#################### SERVIDOR ###########################

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer((IP,PUERTO),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
	def PrestarPagina(self):
		if PaginasDisponibles.length() == 0:
			return 0
		else: 
			Pagina =  PaginasDisponibles[0].remove()
			capacidad = MisPaginas.index(Pagina)
			Archivo = open(Pagina,"r")
			contenido = Archivo.read()
			Archivo.close()
			return contenido, Pagina, capacidad

	def Consistencia(self, nombrearchivo, contenido):
		pagina = open(nombrearchivo,"w")
		pagina.write(contenido)
		pagina.close()
		PaginasDisponibles.append(nombrearchivo)

		return 0

server.register_instance(MyFuncs())

server = xmlrpclib.ServerProxy('http://localhost:8006')
