from Lista_Doble import ListaDoble

class Estudiante(): #class Nodo
    def __init__(self, carnet, nombre):
        self.carnet = carnet
        self.nombre = nombre
        self.cursos = ListaDoble()
        #self.amigos = ListaAmigos()
        self.siguiente = None # Null

    def getCarnet(self):
        return self.carnet

    
    def setCarnet(self, carnet):
        self.carnet = carnet
    
    
    def getSiguiente(self):
        return self.siguiente

    
    def setSiguiente(self, estudiante):
        self.siguiente = estudiante



