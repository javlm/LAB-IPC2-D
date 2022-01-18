from Nodo_Encabezado import Nodo_Encabezado


class Lista_Encabezado():
    def __init__(self, tipo):
        self.primero: Nodo_Encabezado = None
        self.ultimo: Nodo_Encabezado = None
        self.tipo = tipo
        self.size = 0

    def insertar_nodoEncabezado(self, nuevo):
        #nuevo = Nodo_Encabezado(nuevo)
        self.size += 1
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            # ---- Insercion en ORDEN
            # -- verificamos si el nuevo es menor que el primero
            if nuevo.id < self.primero.id:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            # -- verificamos si el nuevo es mayor que el ultimo
            elif nuevo.id > self.ultimo.id:
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            else:
                # -- sino, recorremos la lista para buscar donde acomodarnos, entre el primero y el ultimo
                tmp: Nodo_Encabezado = self.primero 
                while tmp != None:
                    if nuevo.id < tmp.id:
                        nuevo.siguiente = tmp
                        nuevo.anterior = tmp.anterior
                        tmp.anterior.siguiente = nuevo
                        tmp.anterior = nuevo
                        break
                    elif nuevo.id > tmp.id:
                        tmp = tmp.siguiente
                    else:
                        break

    def mostrarEncabezados(self):
        tmp = self.primero
        while tmp != None:
            print('Encabezado', self.tipo, tmp.id)
            tmp = tmp.siguiente

    def getEncabezado(self, id) -> Nodo_Encabezado: #esta funcion debe retornar un nodo cabecera
        tmp = self.primero
        while tmp != None:
            if id == tmp.id:
                return tmp
            tmp = tmp.siguiente
        return None

'''
Filas = Lista_Encabezado('Fila')
n1 = Nodo_Encabezado(8)
Filas.insertar_nodoEncabezado(n1)
Filas.insertar_nodoEncabezado(3)
Filas.insertar_nodoEncabezado(5)
Filas.insertar_nodoEncabezado(4)
Filas.insertar_nodoEncabezado(2)
Filas.insertar_nodoEncabezado(1)
Filas.insertar_nodoEncabezado(7)
Filas.insertar_nodoEncabezado(6)

Filas.mostrarEncabezados()

print(Filas.getEncabezado(10))
'''