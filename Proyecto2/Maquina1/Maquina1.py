from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import random
import time
import threading
import os

IP = '127.0.0.1'
PUERTO = 8007
MisPaginas = ["M1P1.txt", "M1P2.txt", "M1P3.txt"]
Capacidad = [10, 8, 5]


server = xmlrpclib.ServerProxy('http://localhost:8006')
print "Registrando Espacio de Memoria ..."
n = 0
for i in MisPaginas:
	registroPaginas = server.RegistrarPagina(i, IP, PUERTO, Capacidad[n])
	n += 1
	time.sleep(1)

#################### SERVIDOR ###########################

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer((IP,PUERTO),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
	def LeerPagina(self, nombrearchivo):
		pagina = open(nombrearchivo,"r")
		contenido = pagina.read()
		pagina.close()
		return contenido

	def ActualizarPagina(self, nombrearchivo, contenido):
		pagina = open(nombrearchivo,"w")
		pagina.write(contenido)
		pagina.close()
		return 0

	def ListarPagina(self):
		return MisPaginas

server.register_instance(MyFuncs())
