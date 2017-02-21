from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import math

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8007),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def logaritmo_function(dato):
	x, y = dato.split("l")
	log= math.log(int(Dato1), int(Dato2))
	return str(log)
server.register_function(logaritmo_function, 'log')

# Run the server's main loop
server.serve_forever()
