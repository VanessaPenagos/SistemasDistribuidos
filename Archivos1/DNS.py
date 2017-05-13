from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import random

IP = '127.0.0.1'
PORT = 8006
BUFER_SIZE = 20

archivosOriginales = ["Dani.txt", "Vane.txt", "Otro.txt"]
clientes = [8007, 8008]

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer((IP,PORT),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
    def ActualizarArchivo(self, nombrearchivo, contenidoarchivo):
        archivo = open(nombrearchivo,"w")
        archivo.write(contenidoarchivo)
        archivo.close()
        server1 = xmlrpclib.ServerProxy('http://localhost:8007')
        server2 = xmlrpclib.ServerProxy('http://localhost:8008')
        server1.RecibirActualizacion(nombrearchivo, contenidoarchivo)
        server2.RecibirActualizacion(nombrearchivo, contenidoarchivo)
        return 0

	def Bloqueo (self, nombre):
		for archivo in self.archivosCompartidos:
			if archivo.nombre == nombre:
				self.archivosBloqueados.append(archivo)
		return 0

	def Desbloqueo(self, nombre):
		for archivo in self.archivosCompartidos:
			if archivo.nombre == nombre:
				self.archivosBloqueados.remove(archivo)
		return 0
server.register_instance(MyFuncs())

server.serve_forever()
