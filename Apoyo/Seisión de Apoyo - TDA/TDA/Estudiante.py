from ListaDoble import ListaDoble

class Estudiante: #Clase Nodo
    def __init__(self, carnet, nombre):
        self.carnet = carnet
        self.nombre = nombre
        self.lista_cursos = ListaDoble() #otro TDA
        self.siguiente = None

    def getCursos(self):
        return self.lista_cursos


