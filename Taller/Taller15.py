import threading
import time

class Servidor(threading.Thread):
    def __init__(self):
    	threading.Thread.__init__(self)

    def suma(a,b):
        return a + b

    def resta(a,b):
        return a - b

    def mult(a,b):
        return a * b

    def run():
        #Lectura de funcion en el archivo 
        time.sleep(1)
        archivo1 = open("elegida.txt", "r")
        elegida = archivo1.read()
        archivo1.close()
        print elegida


class Cliente(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

    def run():
        archivo = open("funciones.txt", "r")
        for line in archivo:
        	if line == 'mult':
        	archivol = open("elegida.txt", "w")
        	archivol.write(line)
        	archivol.close()
       	archivo.close()

cliente = Cliente()
cliente.start()
servidor = Servidor()
servidor.start()
cliente.run()
servidor.run()


   
