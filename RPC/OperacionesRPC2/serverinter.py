from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

TCP_PORTS = ['8001','8002','8003','8004','8005','8006','8007']
TCP_IPS = ['localhost','localhost','localhost','localhost','localhost','localhost','localhost']

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def operacion(dato):
	if '+' in dato:
		cad='http://'+TCP_IPS[0]+':'+TCP_PORTS[0]
		return cad
	if '-' in dato:
		cad='http://'+TCP_IPS[1]+':'+TCP_PORTS[1]
		return cad
	if '*' in dato:
		cad='http://'+TCP_IPS[2]+':'+TCP_PORTS[2]
		return cad
	if '/' in dato:
		cad='http://'+TCP_IPS[3]+':'+TCP_PORTS[3]
		return cad
	if '^' in dato:
		cad='http://'+TCP_IPS[4]+':'+TCP_PORTS[4]
		return cad
	if 'r' in dato:
		cad='http://'+TCP_IPS[5]+':'+TCP_PORTS[5]
		return cad
	if 'l' in dato:
		cad='http://'+TCP_IPS[6]+':'+TCP_PORTS[6]
		return cad


server.register_function(operacion, 'op')

# Run the server's main loop
server.serve_forever()
