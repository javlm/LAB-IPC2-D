#------------ Nodo que representa el encabezado de una fila y columna respectivamente
class Nodo_Encabezado():
    def __init__(self, id):
        self.id : int = id #posicion de fila o columna
        self.siguiente = None
        self.anterior = None
        self.acceso = None #-- apuntador a los nodos de la matriz(nodos internos)