from ListaDoble import ListaDoble

letras = ListaDoble()

letras.insertar(6, 'F')
letras.insertar(10, 'J')
letras.insertar(5, 'E')
letras.insertar(3, 'C')
letras.insertar(1, 'A')
letras.insertar(8, 'H')
letras.insertar(7, 'G')
letras.insertar(2, 'B')
letras.insertar(4, 'D')
letras.insertar(9, 'I')

letras.mostrarCursos()

#letras.BubbleSortStd()

#letras.BubbleSort()
#print('----------BubbleSort---------')
#letras.mostrarCursos()

#letras.InsertionSort()
#print('----------InsertionSort---------')
#letras.mostrarCursos()

#letras.SelectionSort()
#print('----------SelectionSort---------')
#letras.mostrarCursos2()

letras.QuickSort(letras.inicio, letras.final)
print('----------QuickSort---------')
letras.mostrarCursos()