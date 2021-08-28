from typing import List
from Posicion import Posicion  

class ListaPosiciones():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def insertarPos(self, x, y, val): #insertar
        nuevo = Posicion(x, y, val)
        if self.inicio is None:
            self.inicio = nuevo
            self.fin = nuevo
        else:
            tmp = self.fin
            tmp.siguiente = nuevo
            nuevo.anterior = tmp
            self.fin = nuevo
        return nuevo

    def getPosiciones(self):
        tmp = self.inicio
        while tmp is not None:
            print('x:', tmp.x, 'y:', tmp.y, 'Combustible:', tmp.val)
            tmp = tmp.siguiente

    def getPosicion(self, x,y):
        tmp = self.inicio
        while tmp is not None: #1.s -> 2.s -> 3.s -> 4.s -> None
            if tmp.x == x and tmp.y==y:
                return tmp
            tmp = tmp.siguiente
    
    def getLista(self):
        return self


#l1 = ListaPosiciones()
#print(l1.getLista())
