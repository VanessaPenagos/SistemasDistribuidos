import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
operacion=raw_input('Ingrese la operacion a realizar:' )
direccion = s.op(operacion)

if '+' in operacion:
	s1 = xmlrpclib.ServerProxy(direccion)
	print s1.add(operacion)
if '-' in operacion:
	s1 = xmlrpclib.ServerProxy(direccion)
	print s1.add(operacion)
if '*' in operacion:
	s1 = xmlrpclib.ServerProxy(direccion)
	print s1.add(operacion)
if '/' in operacion:
	s1 = xmlrpclib.ServerProxy(direccion)
	print s1.add(operacion)
if '^' in operacion:
	s1 = xmlrpclib.ServerProxy(direccion)
	print s1.add(operacion)
if 'r' in operacion:
	s1 = xmlrpclib.ServerProxy(direccion)
	print s1.add(operacion)
if 'l' in operacion:
	s1 = xmlrpclib.ServerProxy(direccion)
	print s1.add(operacion)


# Print list of available methods
#print s.system.listMethods()
