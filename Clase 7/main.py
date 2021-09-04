from MatrizDispersa import MatrizDispersa

matriz = MatrizDispersa(0)

'''
matriz.insert(10, 10, '*')
matriz.graficarNeato('PrimerNodo')
matriz.insert(1, 1, '*')
matriz.insert(1, 2, '*')
matriz.insert(1, 3, '*')
matriz.insert(1, 4, '*')
matriz.insert(2, 1, '*')
matriz.insert(2, 2, '*')
matriz.insert(2, 3, '*')
matriz.insert(2, 4, '*')
matriz.insert(3, 1, '*')
matriz.insert(3, 2, '*')
matriz.insert(3, 3, '*')
matriz.insert(3, 4, '*')
matriz.insert(4, 1, '*')
matriz.insert(4, 2, '*')
matriz.insert(4, 3, '*')
matriz.insert(4, 4, '*')
matriz.insert(8, 9, '*')
matriz.insert(9, 8, '*')
matriz.graficarNeato('Final')
'''

def insertaTodo():
    with open('jollyroger.txt') as archivo:
        l = 0
        c = 0
        lineas = archivo.readlines()
        for linea in lineas:
            columnas = linea
            l += 1
            for col in columnas:
                if col != '\n':
                    c += 1
                    matriz.insert(l, c, col)
            c = 0
            matriz.graficarNeato('JollyRoger')

def insertaSeleccion(): #este metodo a diferencia del otro, solo va a insertar nodos en la matriz
                        # cuando en el archivo de entrada, encuentre el caracter '*', los demas, los ignora
    with open('jollyroger.txt') as archivo:
        l = 0
        c = 0
        lineas = archivo.readlines()
        for linea in lineas:
            columnas = linea
            l += 1
            for col in columnas:
                if col != '\n':
                    c += 1
                    if col =='*':
                        matriz.insert(l, c, col)
            c = 0
            matriz.graficarNeato('JollyRoger')

#insertaTodo()
#insertaSeleccion()