from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8001),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def adder_function(dato):
	x, y = dato.split("+")
	suma= int(x) + int(y)
	return str(suma)
server.register_function(adder_function, 'add')

# Run the server's main loop
server.serve_forever()










