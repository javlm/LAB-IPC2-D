class Celda():
    def __init__(self, r, c, color):
        self.row = r #coordenada X o Fila
        self.column = c # coordenada Y o Columna
        self.color = color #blanco/negro w/b
        self.siguiente = None
        self.anterior = None


