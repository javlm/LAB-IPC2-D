from Nodo import Estudiante

class Lista_Simple():
    def __init__(self):
        self.primero : Estudiante = None #cabecera
        self.ultimo = None # final
        self.size = 0

    
    def insertLast(self, carnet, nombre, edad, carrera):
        nuevo_estudiante = Estudiante(carnet, nombre, edad, carrera)
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
        




lista2 = Lista_Simple()
lista2.insertLast(201612098, 'Javier Lima', 15, 'Sistemas')
lista2.insertLast(202010814, 'Luis Garcia', 15, 'Sistemas')
lista2.insertLast(201902502, 'Carlos Soto', 15, 'Sistemas')
lista2.insertLast(201900597, 'Joaquin Ortega', 15, 'Sistemas')
lista2.insertLast(201908169, 'Joshua Muy', 15, 'Sistemas')
lista2.insertLast(202004812, 'Fredy Quijada', 15, 'Sistemas')
lista2.insertLast(202003220, 'Marco Solis', 15, 'Sistemas')
lista2.insertLast(202006688, 'Karla González', 15, 'Sistemas')


lista2.showStudents()

