from Curso import Curso

class ListaDoble():
    def __init__(self):
        self.inicio = None

    def insertar(self, codigo, nombre, creditos): #insertar
        nuevo = Curso(codigo, nombre, creditos)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp

    def mostrarCursos(self):
        tmp = self.inicio
        while tmp is not None:
            print('Codigo:', tmp.codigo, 'Nombre:', tmp.nombre, 'Creditos:', tmp.creditos)
            tmp = tmp.siguiente



