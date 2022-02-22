class Curso():
    def __init__(self, c , n):
        self.cod = c
        self.nombre = n
        self.siguiente = None
        self.anterior = None


    def getSiguiente(self):
        return self.siguiente

    
    def setSiguiente(self, curso):
        self.siguiente = curso

    def getAnterior(self):
        return self.anterior

    
    def setAnterior(self, curso):
        self.anterior = curso