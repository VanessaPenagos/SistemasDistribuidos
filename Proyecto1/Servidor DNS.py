from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

IP = '127.0.0.1'
PORT = 8006
BUFER_SIZE = 20


class Archivo:
	def __init__(self, nombre, direcciona, permiso):
		self.nombre = nombre
		self.permiso = permiso
		self.direcciona = direcciona

class Cliente:
	def __init__(self, ip, puerto) :
		self.archivos = []
		self.direccionip = ip
		self.puerto = puerto

	def EliminarArchivo (self):
		pass

# Create server
server = SimpleXMLRPCServer((IP,PORT),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

class MyFuncs:
	def __init__(self):
		self.recursos = []
	def RegistrarRecursos (self):


server.register_instance(MyFuncs())

server.serve_forever()
