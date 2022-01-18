from ListaDoble import ListaPosiciones

class Terreno:
    def __init__(self, nombre, n, m, ix, iy, fx, fy):
        self.nombre = nombre
        self.n = n 
        self.m = m 
        self.inicioX = ix
        self.inicioY = iy
        self.finX = fx 
        self.finY = fy
        self.listaPosiciones = ListaPosiciones()
        self.camino = ListaPosiciones()
        self.siguiente = None


