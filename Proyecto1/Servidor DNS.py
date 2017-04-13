from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import random

IP = '127.0.0.1'
PORT = 8006
BUFER_SIZE = 20

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class Archivo:
	def __init__(self, nombre, ip, puerto, permiso):
		self.nombre = nombre
		self.permiso = permiso # 0-> escritura , 1-> lectura, 2-> ambos
		self.ipcliente = ip
		self.puertocliente = puerto

class Cliente:
	def __init__(self, ip, puerto) :
		self.archivos = []
		self.direccionip = ip
		self.puerto = puerto

	def AgregarArchivo (self, archivo):
		self.archivos.append(archivo)

class ArchivosCompartidos:
	def __init__ (self, ip, puerto, nombre):
		self.ip = ip
		self.puerto = puerto
		self.nombre = nombre

server = SimpleXMLRPCServer((IP,PORT),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
	def __init__(self):
		self.clientes = []
		self.archivosCompartidos = []

	def RegistrarCliente (self, ip, puerto):
		for cliente in self.clientes:
			if cliente.direccionip == ip and cliente.puerto == puerto:
				return "Cliente ya registrado"
		cliente = Cliente(ip, puerto)
		self.clientes.append(cliente)
		return "Cliente Registrado"

	def RegistrarArchivos (self, nombre, ip, puerto):
		archivo = Archivo(nombre, ip, puerto, 2)
		for a in self.archivosCompartidos:
			if a.nombre == nombre:
				return "Archivo ya registrado"
		for cliente in self.clientes:
			if cliente.direccionip == ip and cliente.puerto == puerto:
					cliente.AgregarArchivo(archivo)
		archivoCompartido = ArchivosCompartidos(ip, puerto, nombre)
		self.archivosCompartidos.append(archivoCompartido)
		return "Archivo "+ nombre +" registrado"

	def ListarArchivos(self):
		pass
		return 0

	def BuscarArchivo (self, nombre):
		pass
		return 0 

	def GenerarPermisos(self):
		pass
		return 0 

	def EliminarArchivos(self):
		pass
		return 0

server.register_instance(MyFuncs())

server.serve_forever()
