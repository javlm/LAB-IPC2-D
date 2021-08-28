from ListaSimple import ListaTerrenos

#raiz -> elemento:terreno1{n,m, posinicio, posfin, [posicion, posicion, posicion,...]}, 
                # elemento:terreno2{n,m, posinicio, posfin, [posicion, posicion, posicion,...]} ...  
                #     elemento:terrenoN{n,m, posinicio, posfin, [posicion, posicion, posicion,...]} 

class Principal: 
    def __init__(self):
        self.ListaTerrenos = ListaTerrenos()
    
    def Menu(self):
        pass

    def CargarArchivo(self):
        raiz = elementTree.getroot()
        for elemento in raiz:
            terreno = self.ListaTerrenos.insertarTerreno(nombre, n, m, ix, iy, fx, fy)
            for subelemento in raiz.iter('posicion'):
                terreno.listaPosiciones.insertarPos(x,y,valor)

    def getListaTerreno(self, nombre):
        terreno = self.ListaTerrenos.getTerreno(nombre);
        listaPos = terreno.listaPosiciones.getLista()
        posinicio = listaPos.getPosicion(terreno.inicioX, terreno.inicioY) 
        terreno.camino.insertarPos(posinicio.x, posinicio.y, posinicio.val)





