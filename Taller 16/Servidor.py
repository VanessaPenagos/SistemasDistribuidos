from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import random

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

IP = '127.0.0.1'
PORT = 8006
BUFER_SIZE = 20


# Create server
server = SimpleXMLRPCServer((IP,PORT),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

tareas = ['1','2','3','4','5','6']
print "Esperando a que sirva"

class MyFuncs:
	def Disponibilidad(self,estado):
		print "El estado es",estado
		if estado == '0':
			print "aqui empieza"
			n = random.randint(1,6)
			print "Este es el random ", n
			if n in tareas:
				print "aqui paso"
				t = tareas.index(n)
				tareas.pop(t)
			return n
		else:
			print "No existen estaciones disponibles"
			return 'no'

server.register_instance(MyFuncs())

server.serve_forever()
