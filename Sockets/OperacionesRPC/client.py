import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
operacion=raw_input('Ingrese la operacion a realizar:' )
print s.op(operacion)

# Print list of available methods
print s.system.listMethods()
