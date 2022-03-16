
class Nodo_Cabecera():
    def __init__(self, id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None

    def getAcceso(self):
        return self.acceso

    def setAcceso(self, nuevo_acceso):
        self.acceso = nuevo_acceso