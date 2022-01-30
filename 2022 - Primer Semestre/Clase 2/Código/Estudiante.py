from Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carnet):
        super().__init__(nombre, apellido, edad)
        self.carnet = carnet

        
    def hablar2(self):
        self.hablar()
        print('Sale en vacas')