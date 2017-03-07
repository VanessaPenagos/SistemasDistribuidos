from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def operacion(dato):
	if '+' in dato:
		s = xmlrpclib.ServerProxy('http://localhost:8001')
		return s.add(dato)
	if '-' in dato:
		s = xmlrpclib.ServerProxy('http://localhost:8002')
		return s.res(dato)
	if '*' in dato:
		s = xmlrpclib.ServerProxy('http://localhost:8003')
		return s.mult(dato)
	if '/' in dato:
		s = xmlrpclib.ServerProxy('http://localhost:8004')
		return s.div(dato)
	if '^' in dato:
		s = xmlrpclib.ServerProxy('http://localhost:8005')
		return s.pot(dato)
	if 'r' in dato:
		s = xmlrpclib.ServerProxy('http://localhost:8006')
		return s.raiz(dato)
	if 'l' in dato:
		s = xmlrpclib.ServerProxy('http://localhost:8007')
		return s.log(dato)


server.register_function(operacion, 'op')

# Run the server's main loop
server.serve_forever()
