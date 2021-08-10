from Estudiante import Estudiante

class ListaSimple():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def crearEstudiante(self, carnet, nombre):  #insertar a final
        nuevo = Estudiante(carnet, nombre) #nuevo estudiante
        self.size += 1
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def mostrarEstudiantes(self):
        tmp = self.inicio
        while tmp is not None:
            print('Carnet:', tmp.carnet, 'Nombre:',tmp.nombre)
            tmp = tmp.siguiente

    def eliminarEstudiante(self, carnet):
        tmp = self.inicio
        while tmp is not None:
            if tmp.carnet == carnet:
                self.inicio = tmp.siguiente
                tmp.siguiente = None
                print('Estudiante',carnet, 'eliminado.')
                break
            elif tmp.siguiente is not None:
                if tmp.siguiente.carnet == carnet:
                    Nodo_a_borrar = tmp.siguiente
                    tmp.siguiente = Nodo_a_borrar.siguiente
                    Nodo_a_borrar.siguiente = None
                    print('Estudiante', carnet,'eliminado.')
                    break
            tmp = tmp.siguiente

    def getEstudiante(self, carnet):
        tmp = self.inicio
        while tmp is not None:
            if tmp.carnet == carnet:
                return tmp
            tmp = tmp.siguiente
        return None

