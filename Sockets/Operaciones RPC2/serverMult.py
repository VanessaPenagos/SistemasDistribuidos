from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8003),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def multiplicacion_function(dato):
	x, y = dato.split("*")
	mult = int(x) * int(y)
	return str(mult)
server.register_function(multiplicacion_function, 'mult')

# Run the server's main loop
server.serve_forever()


