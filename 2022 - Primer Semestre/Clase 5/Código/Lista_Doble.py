from NodoCurso import Curso

class ListaDoble():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertarCursoAlFinal(self, cod, nombre):
        nuevo_curso = Curso(cod, nombre) # primer paso
        self.size += 1
        if self.primero is None:
            self.primero = nuevo_curso
            self.ultimo = nuevo_curso 
        else: 
            self.ultimo.setSiguiente(nuevo_curso)
            nuevo_curso.setAnterior(self.ultimo)
            self.ultimo = nuevo_curso
           

    def mostrarCursos(self):
        tmp = self.primero
        while tmp is not None:
            print('Cod', tmp.cod, 'Nombre:',tmp.nombre)
            tmp = tmp.getSiguiente()