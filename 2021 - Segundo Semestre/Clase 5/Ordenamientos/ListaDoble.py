from Letra import Letter

class ListaDoble():
    def __init__(self):
        self.inicio = None
        self.final = None
        self.size = 0
    
    def insertar(self, num, char): #insertar
        nuevo = Letter(num, char)
        self.size += 1
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp
            self.final = nuevo

    def clear(self):
        self.inicio = None

    def mostrarCursos(self):
        tmp = self.inicio
        while tmp is not None:
            print('No:', tmp.num, 'Caracter:', tmp.char)
            tmp = tmp.siguiente


    def mostrarCursos2(self):
        tmp = self.inicio
        for i in range(self.size):
            print('No:', tmp.num, 'Caracter:', tmp.char)
            tmp = tmp.siguiente


    def BubbleSortStd(self):
        comprobar = self.inicio
        aux = self.inicio
        if comprobar.siguiente != None and aux != None:
            i = self.inicio
            while i != None:
                j = i.siguiente
                while j != None:
                    if i.num > j.num:
                        temporal = i.num
                        i.num = j.num
                        j.num = temporal
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
                    if actual.num > j.num:
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


    def InsertionSort(self):
        tmp = self.inicio
        while tmp != None: # ->
            i = tmp
            j = tmp.siguiente
            cambio = False
            while j != None and i.num > j.num: # <-
                cambio = True
                if i.anterior != None and j.siguiente != None: # Para cambios entre nodos
                    i.anterior.siguiente = j
                    i.siguiente = j.siguiente
                    j.siguiente.anterior = i
                    j.anterior = i.anterior
                    i.anterior = j
                    j.siguiente = i
                    i = j.anterior
                elif j.siguiente == None: # Cambios de ultimo nodo hacia atras
                    i.anterior.siguiente = j
                    j.anterior = i.anterior
                    j.siguiente = i
                    i.anterior = j
                    i.siguiente = None
                    i = self.inicio
                    break
                else: #cambios al principio de la lista
                    j.siguiente.anterior = i
                    i.anterior = j
                    i.siguiente = j.siguiente
                    j.anterior = None
                    j.siguiente  = i
                    self.inicio = j
                    break
            if cambio:
                tmp = i
            else:
                tmp = tmp.siguiente


    def SelectionSort(self):
        peq = self.inicio
        tmp = peq
        for i in range(self.size-1):
            actual = tmp.siguiente
            for j in range(i+1, self.size):
                if actual.num < peq.num:
                    peq = actual
                actual = actual.siguiente
            self.exchange(tmp, peq)
            tmp = tmp.siguiente
            peq = tmp

    def exchange(self, a, b):
        tmp = Letter(a.num, a.char)
        a.setAttr(b.num, b.char)
        b.setAttr(tmp.num, tmp.char)
        del tmp

    def QuickSort(self, nodoizq, nododer):
        pivote = Letter(nodoizq.num, nodoizq.char)
        i = -1
        j = -1
        nodoi = nodoizq
        nodoj = nododer
        actual = self.inicio
        while actual != None:
            i += 1
            if actual == nodoizq: break
            actual = actual.siguiente

        actual = self.inicio
        while actual != None:
            j += 1
            if actual == nododer: break
            actual = actual.siguiente
        izq = i
        der = j
        while i<j:
            while nodoi.num <= pivote.num and i<j:
                i += 1
                nodoi = nodoi.siguiente
            while nodoj.num > pivote.num:
                j -= 1
                nodoj = nodoj.anterior
            if i < j:
                aux = Letter(nodoi.num, nodoi.char)
                nodoi.setAttr(nodoj.num, nodoj.char)
                nodoj.setAttr(aux.num, aux.char)

        nodoizq.setAttr(nodoj.num, nodoj.char)
        nodoj.setAttr(pivote.num, pivote.char)

        if izq < j - 1:
            self.QuickSort(nodoizq, nodoj.anterior)
        if j + 1 < der:
            self.QuickSort(nodoj.siguiente, nododer)