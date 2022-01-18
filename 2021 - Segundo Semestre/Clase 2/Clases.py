class Persona():
    atributo = 'Hola, soy una persona'
    def __init__(self, apellido, edad):
        #atributos_instancia
        self.__nombre = None
        self.apellido = apellido
        self.edad = edad

    def setNombre(self, name):
        self.__nombre = name

    def getNombre(self):
        return self.__nombre

    def Existir(self):
        pass

    def Hablar(self):
        print(self.atributo, 'mi nombre es:', self.getNombre(), 'cuya dedicacion es ->', type(self).__name__);

class Estudiante(Persona):
    def __init__(self, apellido, edad, carnet, carrera):
        super().__init__(apellido, edad)
        self.carnet = carnet
        self.carrera = carrera

    def Hablar(self):
        print(self.atributo, 'cuya dedicacion es ->', type(self).__name__, ' y estudio la carrera de', self.carrera);

class Profesor(Persona):
    def Hablar(self):
        print('Soy un profesor jeje')

class Curso():
    def __init__(self):
        pass

    def codigo(self):
        print('0771')

p1 = Persona('Lopez', 25)
p1.setNombre('Fernando')
p1.Hablar()

st1 = Estudiante('Lima', 23, 201612098, 'Ing. Industrial')
st1.setNombre('Javier Estuardo')
st1.Hablar()

prof1 = Profesor('Espino', 60) 
prof1.Hablar()

c1 = Curso()
c1.codigo()