class Vehiculo:
    def __init__(self, modelo, marca, color, precio):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.precio = precio
        self.siguiente = None
        self.anterior = None

v1 = Vehiculo('Civic','Honda','Negro',75000)
v2 = Vehiculo('Gemera','Koenisseg','Negro',13938557)
v3 = Vehiculo('Corolla','Toyota','Rojo',110000)
v4 = Vehiculo('RAV4','Toyota','Perla',200000)
vehiculos = []
vehiculos.append(v1)
vehiculos.append(v2)
vehiculos.append(v3)
vehiculos.append(v4)

for v in vehiculos:
    print(v.siguiente)

class ListaEnlazada:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.size = 0

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.inicio == None

    def append(self, marca, modelo, color, precio):
        nuevo = Vehiculo(marca, modelo, color, precio)
        self.size += 1
        if self.isEmpty():
            self.inicio = nuevo
            self.final = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None: #!=None
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp
            self.final = nuevo

    def showCars(self):
        tmp = self.inicio
        while tmp is not None:
            print(tmp.marca, tmp.modelo, tmp.color)
            tmp = tmp.siguiente
        
    
    def shoeCarsInverse(self):
        tmp = self.final
        while tmp is not None:
            print(tmp.marca, tmp.modelo, tmp.color)
            tmp = tmp.anterior

    def crearReporte(self):
        tmp = self.inicio
        contenido = '''digraph G {
    style=filled;
    color=lightgrey;
    node [style=filled,color=white];
   '''
        r = open('reporte.txt','w')
        while tmp is not None:
            contenido += 'nodo1[caracteristicas] \n'
            tmp = tmp.siguiente
        contenido+='\n}'
        r.write(contenido)
        r.close()

    


vehiculos2 = ListaEnlazada()
vehiculos2.append('Civic','Honda','Negro',75000)
vehiculos2.append('Gemera','Koenisseg','Negro',13938557)
vehiculos2.append('Corolla','Toyota','Rojo',110000)
print('>Normal')
vehiculos2.showCars()
print('>Inverso')
vehiculos2.shoeCarsInverse()
vehiculos2.crearReporte()