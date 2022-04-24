from mascota import Mascota

class Manager():
    def __init__(self):
        self.mascotas = []
        self.positivos = []
        self.negativos = []
        self.empresas = []


    def agregar_mascota(self, n, a, e):
        nuevo = Mascota(n, a, e)
        self.mascotas.append(nuevo)

    
    def obtener_mascotas(self):
        json = []
        for mascota in self.mascotas:
            mascota = {
                'nombre' : mascota.nombre,
                'tipo' : mascota.animal,
                'edad' : mascota.edad
            }
            json.append(mascota)
        return json

    def crearArchivoAlmacenamiento(self):
        pass

    def resumenporFecha(self, fecha, empresa, empresas):
        pass

    def resumenporRangoFecha(self, fecha1, fecha2, empresa, empresas):
        pass