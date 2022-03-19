from MatrizDispersa import MatrizDispersa

matriz = MatrizDispersa()

matriz.insertar(1, 1, 'Andre')     
matriz.insertar(1, 2, 'Jose Jorge')
matriz.insertar(1, 3, 'Nathan')
matriz.insertar(1, 4, 'Kemel')
matriz.insertar(2, 1, '*')
matriz.insertar(2, 2, '*')
matriz.insertar(2, 3, '*')
matriz.insertar(2, 4, '*')
matriz.insertar(3, 1, '*')
matriz.insertar(3, 2, 'hola')
matriz.insertar(3, 3, '*')
matriz.insertar(3, 4, '*')
matriz.insertar(4, 1, '*')
matriz.insertar(4, 2, '*')
matriz.insertar(4, 3, '*')
matriz.insertar(4, 4, '*')
matriz.insertar(8, 9, '*')
matriz.insertar(9, 8, '*')
matriz.insertar(2, 2, '*')
matriz.insertar(15,20,'*')
matriz.insertar(15,2, 'Luis Enrique')
matriz.insertar(15,4,'*')

#matriz.graficarNeato('Matriz Dispersa')

matriz.recorridoPorFila(50)
#matriz.recorridoPorColumna(2)

#NodoEncontrado = matriz.ubicarCoordenada(50,20)

print('Hola mundo')