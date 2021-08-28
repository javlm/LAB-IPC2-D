from Terreno import Terreno

class ListaTerrenos(): 
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def insertarTerreno(self, nombre, n, m, ix, iy, fx, fy): 
        nuevo = Terreno(nombre, n, m, ix, iy, fx, fy) 
        self.size += 1
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
        return nuevo

    def getTerreno(self, nombre):
        tmp = self.inicio
        for x in range(self.size):
            if tmp.nombre == nombre:
                return tmp
            tmp = tmp.siguiente