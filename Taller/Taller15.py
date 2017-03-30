import threading
import time

class Servidor(threading.Thread):
    def __init__(self):
    	threading.Thread.__init__(self)

    def suma(self,a,b):
        return int(a) + int(b)

    def resta(self,a,b):
        return int(a) - int(b)

    def mult(self,a,b):
        return int(a) * int(b)

    def run(self):
    	#Lectura de funcion en el archivo 
    	time.sleep(1)
        archivo1 = open("elegida.txt", "r")
        elegida = archivo1.read()
        archivo1.close()
        operacion,a,b = elegida.split()
        if operacion == 'mult':
        	resultado = self.mult(a,b)
        if operacion == 'suma':
        	resultado = self.suma(a,b)
        if operacion == 'resta':
        	resultado = self.resta(a,b)
      	archivo2 = open("resultado.txt", "w")
      	archivo2.write(str(resultado))
      	archivo2.close()

class Cliente(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		archivo = open("funciones.txt", "r")
		for line in archivo:
			if line == 'mult':
				archivol = open("elegida.txt", "w")
				archivol.write(line)
				archivol.write(' 2 3')
		archivol.close()
		archivo.close()
		time.sleep(1)
		archivor = open("resultado.txt", "r")
		resultadof =archivor.read()
		print "El resultado de la operacion es: ",resultadof

cliente = Cliente()
cliente.start()
servidor = Servidor()
servidor.start()


   
