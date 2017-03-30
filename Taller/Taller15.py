import threading

class Servidor(threading.Thread):
    def __init__(self, archivo):
    threading.Thread.__init__(self)
    self.archivo = archivo
    self.stoprequest = threading.Event()

    def suma(a,b):
        return a + b

    def resta(a,b):
        return a - b

    def mult(a,b):
        return a * b

    def run():
        #Escritura de funciones en el archivo
        archivo1 = open("hola.txt", "w")
        contenido = archivo1.write('suma$resta$mult')
        archivo1.close()

class Cliente(threading.Thread):
    def __init__(self, archivo):
    threading.Thread.__init__(self)
    self.archivo = archivo
    self.stoprequest = threading.Event()

    def run():
        archivo = open("hola.txt", "w")

   
