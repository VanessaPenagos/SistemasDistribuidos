import xmlrpclib
import time

s = xmlrpclib.ServerProxy('http://localhost:8000')
permiso, procesador = s.PedidoProcesador(0)
if permiso == 1:
	time.sleep(2)
	s.DevolverProcesador(procesador)