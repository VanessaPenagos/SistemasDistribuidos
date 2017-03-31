import xmlrpclib
import random
import time

while True:
	s = xmlrpclib.ServerProxy('http://localhost:8006')
	resource = random.randint(1,6)
	print "Recurso Solicitado ", resource
	result = s.QuitResources(str(resource))
	time.sleep(5)
	resultadd = s.AddResources(str(resource))
	print "Respuesta Servidor ", result
