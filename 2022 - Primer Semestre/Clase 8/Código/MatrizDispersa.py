from Nodo_Cabecera import Nodo_Cabecera
from Lista_Cabecera import Lista_Cabecera
import os
import webbrowser

# -----------------------------Codigo de MATRIZ DISPERSA ----------------
# -------- Clase NodoOrtogonal, con 4 apuntadores -> Nodos Internos

class Nodo_Celda(): # Nodos ortogonales
    def __init__(self, x, y, caracter):# 'caracter' puede ser cualquier valor
        self.caracter = caracter
        self.coordenadaX = x  # fila
        self.coordenadaY = y  # columna
        self.arriba = None
        self.abajo = None
        self.derecha = None  # self.siguiente
        self.izquierda = None  # self.anterior

    def setArriba(self, arriba):
        self.arriba = arriba
    

    def getArriba(self):
        return self.arriba
    

    def setAbajo(self, abajo):
        self.abajo = abajo
    

    def getAbajo(self):
        return self.abajo


    def setDerecha(self, derecha):
        self.derecha = derecha
    

    def getDerecha(self):
        return self.derecha
    

    def setIzquierda(self, izquierda):
        self.izquierda = izquierda
    

    def getIzquierda(self):
        return self.izquierda


class MatrizDispersa():
    def __init__(self):
        self.capa = 0
        self.filas = Lista_Cabecera('fila')
        self.columnas = Lista_Cabecera('columna')

    # (filas = x, columnas = y)
    def insertar(self, pos_x, pos_y, caracter):
        nueva_celda = Nodo_Celda(pos_x, pos_y, caracter) # se crea nodo celda a insertar
        # --- lo prinero sera buscar si ya existen los cabeceras en la matriz
        nodo_X = self.filas.getCabecera(pos_x)
        nodo_Y = self.columnas.getCabecera(pos_y)

        if nodo_X == None: # --- comprobamos que el cabecera fila pos_x exista
             # --- si nodo_X es nulo, quiere decir que no existe cabecera fila pos_x
            nodo_X = Nodo_Cabecera(pos_x)
            self.filas.insertar_nodoCabecera(nodo_X)

        if nodo_Y == None: # --- comprobamos que el cabecera columna pos_y exista
            # --- si nodo_Y es nulo, quiere decir que no existe  columna pos_y
            nodo_Y = Nodo_Cabecera(pos_y)
            self.columnas.insertar_nodoCabecera(nodo_Y)

        # ----- INSERTAR NUEVA_CELDA EN FILA
        if nodo_X.getAcceso() == None: # -- comprobamos que el nodo_x no esta apuntando hacia ningun nodoInterno
            nodo_X.setAcceso(nueva_celda)
        else: # -- si esta apuntando, validamos si la posicion de la columna del nueva_celda nodoInterno es menor a la posicion de la columna del acceso 
            if nueva_celda.coordenadaY < nodo_X.getAcceso().coordenadaY: # F1 --->  NI 1,1     NI 1,3      
                nueva_celda.setDerecha(nodo_X.getAcceso())        
                nodo_X.getAcceso().setIzquierda(nueva_celda)
                nodo_X.setAcceso(nueva_celda)
            else:
                #de no cumplirse debemos movernos de izquierda a derecha buscando donde posicionar el nueva_celda nodoInterno
                tmp : Nodo_Celda = nodo_X.getAcceso() 
                while tmp != None:                      
                    if nueva_celda.coordenadaY < tmp.coordenadaY:
                        nueva_celda.setDerecha(tmp)
                        nueva_celda.setIzquierda(tmp.getIzquierda())
                        tmp.getIzquierda().setDerecha(nueva_celda)
                        tmp.setIzquierda(nueva_celda)
                        break;
                    elif nueva_celda.coordenadaX == tmp.coordenadaX and nueva_celda.coordenadaY == tmp.coordenadaY: #validamos que no haya repetidas
                        break;
                    else:
                        if tmp.getDerecha() == None:
                            tmp.setDerecha(nueva_celda)
                            nueva_celda.setIzquierda(tmp)
                            break;
                        else:
                            tmp = tmp.getDerecha() 
                           
        # ----- INSERTAR NUEVA_CELDA EN COLUMNA
        if nodo_Y.getAcceso() == None:  # -- comprobamos que el nodo_y no esta apuntando hacia ningun nodoCelda
            nodo_Y.setAcceso(nueva_celda)
        else: # -- si esta apuntando, validamos si la posicion de la fila del nueva_celda nodoCelda es menor a la posicion de la fila del acceso 
            if nueva_celda.coordenadaX < nodo_Y.getAcceso().coordenadaX:
                nueva_celda.setAbajo(nodo_Y.getAcceso())
                nodo_Y.getAcceso().setArriba(nueva_celda)
                nodo_Y.setAcceso(nueva_celda)
            else:
                # de no cumplirse, debemos movernos de arriba hacia abajo buscando donde posicionar el nueva_celda
                tmp2 : Nodo_Celda = nodo_Y.getAcceso()
                while tmp2 != None:
                    if nueva_celda.coordenadaX < tmp2.coordenadaX:
                        nueva_celda.setAbajo(tmp2)
                        nueva_celda.setArriba(tmp2.getArriba())
                        tmp2.getArriba().setAbajo(nueva_celda)
                        tmp2.setArriba(nueva_celda)
                        break
                    elif nueva_celda.coordenadaX == tmp2.coordenadaX and nueva_celda.coordenadaY == tmp2.coordenadaY: #validamos que no haya repetidas
                        break;
                    else:
                        if tmp2.getAbajo() == None:
                            tmp2.setAbajo(nueva_celda)
                            nueva_celda.setArriba(tmp2)
                            break
                        else:
                            tmp2 = tmp2.getAbajo()
        ##------ Fin de insercion

    def recorridoPorFila(self, fila):
        inicio : Nodo_Cabecera = self.filas.getCabecera(fila)
        if inicio == None:
            print('Esa coordenada de filas no existe')
            return None
            
        tmp : Nodo_Celda = inicio.getAcceso()
        #tmp = self.filas.getCabecera(fila).getAcceso()
        while tmp != None:
            print(tmp.caracter)
            tmp = tmp.getDerecha()

    
    def recorridoPorColumna(self, columna):
        inicio : Nodo_Cabecera = self.columnas.getCabecera(columna)
        if inicio == None:
            print('Esa coordenada de columna no existe')
            return None

        tmp : Nodo_Celda = inicio.getAcceso()
        #tmp = self.filas.getCabecera(fila).getAcceso()
        while tmp != None:
            print(tmp.caracter)
            tmp = tmp.getAbajo()


    def ubicarCoordenada(self, fila, columna):
        try:
            tmp : Nodo_Celda = self.filas.getCabecera(fila).getAcceso()
            while tmp != None:
                if tmp.coordenadaX == fila and tmp.coordenadaY == columna:
                    return tmp
                tmp = tmp.getDerecha()
            return None
        except:
            print('Coordenada no encontrada')
            return None


    def graficarNeato(self, nombre):
        contenido = '''digraph G{
    node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
    edge[style = "bold"]
    node[label = "capa:''' + str(self.capa) +'''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{}" \nfontname="Arial Black" \nfontsize="25pt" \n
                    \n'''.format('\nMATRIZ DISPERSA')

        # --graficar nodos CABECERA
        # --graficar nodos fila
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            contenido += '\n\tnode[label = "F{}" fillcolor="azure3" pos="-1,-{}!" shape=box]x{};'.format(pivote.id, 
            posx, pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            contenido += '\n\tx{}->x{};'.format(pivote.id, pivote.siguiente.id)
            contenido += '\n\tx{}->x{}[dir=back];'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{};'.format(self.filas.primero.id)

        # --graficar nodos columna
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            contenido += '\n\tnode[label = "C{}" fillcolor="azure3" pos = "{},1!" shape=box]y{};'.format(pivotey.id, 
            posy, pivotey.id)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            contenido += '\n\ty{}->y{};'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=back];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{};'.format(self.columnas.primero.id)

        #ya con las cabeceras graficadas, lo siguiente es los nodos internos, o nodosCelda
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda : Nodo_Celda = pivote.acceso
            while pivote_celda != None:
                # --- buscamos posy
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY: break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.caracter == '*':
                    contenido += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                else:
                    contenido += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    ) 
                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.derecha != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha
        
            contenido += '\n\tx{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\tx{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
        
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda : Nodo_Celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY) 
                pivote_celda = pivote_celda.abajo
            contenido += '\n\ty{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\ty{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
                
        contenido += '\n}'
        #--- se genera DOT y se procede a ecjetuar el comando
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}.pdf".format(nombre)
        os.system("neato -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)        