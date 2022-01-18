class Posicion:
    def __init__(self,x , y, val):
        self.x = x
        self.y = y
        self.val = val #combustible
        self.siguiente = None
        self.anterior = None

#Posicion es una clase, plantilla, para los nodos de la ListaDoble de posiciones