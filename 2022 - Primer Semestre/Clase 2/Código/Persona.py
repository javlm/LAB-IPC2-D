class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = None

    def setGenero(self, genero):
        self.genero = genero

    def getGenero(self):
        return self.genero
    
    def hablar(self):
        print('Hola mi nombre es:', self.nombre)




