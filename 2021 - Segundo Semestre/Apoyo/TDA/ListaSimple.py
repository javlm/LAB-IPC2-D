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
            
            
    def BubbleSortStd(self):
        comprobar = self.primero
        aux = self.primero
        if comprobar.siguiente != None and aux != None:
            i = self.primero
            while i != None:
                j = i.siguiente
                while j != None:
                    if i.carnet > j.carnet:
                        temporal = i.carnet
                        i.carnet = j.carnet
                        j.carnet = temporal
                    j = j.siguiente
                i = i.siguiente

    def BubbleSort(self):
        if self.size > 1:
            while True:
                actual = self.inicio
                i = None  # anterior
                j = self.inicio.siguiente  # siguiente
                cambio = False
                while j != None:
                    if actual.carnet > j.carnet:
                        cambio = True
                        if i != None:
                            tmp = j.siguiente
                            i.siguiente = j
                            j.siguiente = actual
                            actual.siguiente = tmp
                        else:
                            tmp2 = j.siguiente
                            self.inicio = j
                            j.siguiente = actual
                            actual.siguiente = tmp2
                        i = j
                        j = actual.siguiente
                    else:
                        i = actual
                        actual = j
                        j = j.siguiente
                if not cambio:
                    break


    def QuickSort(self):
        pass

    def Insertion(self):
        pass
    
    def getEstudiante(self, carnet):
        tmp = self.inicio
        while tmp is not None:
            if tmp.carnet == carnet:
                return tmp
            tmp = tmp.siguiente
        return None

