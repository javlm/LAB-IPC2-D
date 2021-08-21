lista = []
dicccionario = {}
tupla = ()

class Clase():
    def __init__(self, *args): #*args recibe una Tuple(), significa que puede recibir N cantidad de parametros
        if len(args) == 2:
            self.a = args[0]
            self.b = args[1]
        elif len(args) == 3:
            self.x = args[0]
            self.y = args[0]
            self.z = args[0]

class Personaje():
    def __init__(self, nombre, edad, *args):
        self.nombre = nombre
        self.edad = edad
        for x in range(len(args)):
           self.__dict__['atributo' + str(x+3)] = args[x] 

personaje1 = Personaje('Monkey D. Luffy', 19, 'One Piece')
personaje2 = Personaje('Naruto Uzumaki', 25, 'Boruto', 'Naruto', 'Naruto Shippuden')

#for i in personaje1.__dict__.items():
#    print(i)

def sumar(*args):
    suma = 0
    for x in args:
        suma += int(x) 
    return suma

#print(sumar(5,5,5,5,5))

class Persona():
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

persona1 = Persona(nombre='Karla', edad=25, nota=60.9)
persona2 = Persona(nombre='Byron', edad=35)
print(persona2.nombre)


def convertir(**kwargs):
    print(kwargs["simbolo"])

convertir(simbolo='Q')

def metodo(edd):
    print(edd)

metodo(dicccionario)
metodo(lista)
