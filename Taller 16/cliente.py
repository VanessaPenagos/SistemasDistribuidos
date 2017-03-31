import xmlrpclib
import random
import time

# 0 -> disponible
# 1 -> ocupado

while True:
	s = xmlrpclib.ServerProxy('http://localhost:8006')
	estado = random.randint(0,1)
	print "Estado: ", estado
	result = s.Disponibilidad(str(estado))
	if result != 'no':
		time.sleep(result)
	print "Tarea realizada ", result
