from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import random

IP = '127.0.0.1'
PORT = 8006
BUFER_SIZE = 20

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class Pagina:
	def __init__(self, nombre, ip, puerto, capacidad):
		self.nombre = nombre
		self.ipcliente = ip
		self.capacidad = capacidad
		self.puerto = puerto

server = SimpleXMLRPCServer((IP,PORT),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
	def __init__(self):
		self.paginas = []
		self.paginasBloqueadas = []

	def RegistrarPagina (self, nombre, ip, puerto, capacidad):
		pagina = Pagina(nombre, ip, puerto, capacidad)
		self.paginas.append(pagina)
		return nombre

	def Propietario (self, nombre):
		for pagina in self.paginas:
			if pagina.nombre == nombre:
				propietario = ip+":"+str(puerto)
				return propietario
			else
				return "no"
				
	def ListarPagina(self):
		for pag in self.paginas:
			pag.nombre

	def Bloqueo (self, nombre):
		for pagina in self.paginas:
			if pagina.nombre == nombre:
				self.paginasBloqueadas.append(archivo) 
		return 0

	def Desbloqueo(self, nombre):
		for pagina in self.paginas:
			if pagina.nombre == nombre:
				self.paginasBloqueadas.remove(archivo) 
		return 0

server.register_instance(MyFuncs())

server.serve_forever()
