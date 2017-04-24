from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import random

IP = '127.0.0.1'
PORT = 8006
BUFER_SIZE = 20

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class Archivo:
	def __init__(self, nombre, ip, puerto):
		self.nombre = nombre
		self.ipcliente = ip
		self.puertocliente = puerto

class Cliente:
	def __init__(self, ip, puerto) :
		self.archivos = []
		self.direccionip = ip
		self.puerto = puerto

	def AgregarArchivo (self, archivo):
		self.archivos.append(archivo)

	def ElimnarArchivo (self, archivo):
		for elarchivo in self.archivos:
			if archivo == elarchivo:
				self.archivos.remove(elarchivo)

class ArchivosCompartidos:
	def __init__ (self, ip, puerto, nombre):
		self.ip = ip
		self.puerto = puerto
		self.nombre = nombre
		self.permisoescritura = []
		self.permisoescritura.append(ip+":"+str(puerto))

server = SimpleXMLRPCServer((IP,PORT),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
	def __init__(self):
		self.clientes = []
		self.archivosCompartidos = []
		self.archivosBloqueados = []

	def RegistrarCliente (self, ip, puerto):
		for cliente in self.clientes:
			if cliente.direccionip == ip and cliente.puerto == puerto:
				return "Cliente ya registrado"
		cliente = Cliente(ip, puerto)
		#Permisos
		for p in self.archivosCompartidos:
			permiso = random.randint(0,1)
			if permiso == 1:
				p.permisoescritura.append(ip+":"+str(puerto))
		self.clientes.append(cliente)
		return "Cliente Registrado"

	def RegistrarArchivos (self, nombre, ip, puerto):
		archivo = Archivo(nombre, ip, puerto)
		for a in self.archivosCompartidos:
			if a.nombre == nombre:
				return "Archivo ya registrado"
		for cliente in self.clientes:
			if cliente.direccionip == ip and cliente.puerto == puerto:
					cliente.AgregarArchivo(archivo)
		archivoCompartido = ArchivosCompartidos(ip, puerto, nombre)
		#Permisos
		for p in self.clientes:
			permiso = random.randint(0,1)
			direccion = p.direccionip+":"+str(p.puerto)
			direccion2 = ip+":"+str(puerto)
			if permiso == 1 and direccion != direccion2:
				archivoCompartido.permisoescritura.append(direccion)
		self.archivosCompartidos.append(archivoCompartido)
		print "El archivo "+ nombre +" ha sido registrado"

		return nombre

	def ListarArchivos(self):
		lista = []
		for i in self.archivosCompartidos:
			lista.append(i.nombre)
			print i.permisoescritura," Estos son los permisos de ", i.nombre
		return lista

	def BuscarArchivo (self, nombre, dir_entrada):
		permiso = 0
		for bloqueo in self.archivosBloqueados:
			if bloqueo.nombre == nombre:
				return "Nope", permiso
		for value in self.archivosCompartidos:
			if value.nombre == nombre:
				direccion = "http://"+value.ip+":"+str(value.puerto)
				if dir_entrada in value.permisoescritura:
					permiso = 1
				return direccion, permiso
		return "Nope"

	def EliminarArchivos(self, nombre):
		for value in self.archivosCompartidos:
			if value.nombre == nombre:
				ip = value.ip
				puerto = value.puerto
				self.archivosCompartidos.remove(value)
		for cliente in self.clientes:
			if cliente.direccionip == ip and cliente.puerto == puerto:
				cliente.ElimnarArchivo(nombre)
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
