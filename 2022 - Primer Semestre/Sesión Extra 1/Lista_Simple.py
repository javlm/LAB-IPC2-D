from Nodo import Estudiante

class Lista_Simple():
    def __init__(self):
        self.primero : Estudiante = None #cabecera
        self.ultimo = None # final
        self.size = 0

    
    def insertLast(self, carnet, nombre):
        nuevo_estudiante = Estudiante(carnet, nombre)
        self.size += 1
        if self.primero is None:
            self.primero = nuevo_estudiante
            self.ultimo = nuevo_estudiante
        else:
            # Inserción con un solo apuntador "primero"
            '''tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.getSiguiente()
            tmp.setSiguiente(nuevo_estudiante) '''
            
            # Inercion con apuntador "primero"  y "ultimo"
            self.ultimo.setSiguiente(nuevo_estudiante)
            self.ultimo = nuevo_estudiante


    def showStudents(self):
        tmp = self.primero
        for i in range(self.size):
            print(i, 'Carnet:', tmp.getCarnet(), 'Nombre:', tmp.nombre)
            tmp = tmp.getSiguiente()

