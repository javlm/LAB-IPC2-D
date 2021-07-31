

def leerArchivo1(ruta):
    print('------ Lectura archivo #1 -----')
    archivo = open(ruta, encoding='utf-8')
    print(archivo)
    contador = 0
    contenido = ''
    for line in archivo:
        contador = contador + 1
        contenido += line
    print('Lineas contabilizadas: ' + str(contador))
    print(contenido)
    archivo.close()


def leerArchivo2(ruta):
    print('------ Lectura archivo #2 -----')
    with open(ruta, encoding='utf-8') as archivo:
        print(archivo.read())


def leerArchivo3(ruta):
    print('------- Apertura de Archivo usando Try / Except-------')
    try:
        with open(ruta, encoding='utf-8') as file:
            contenido = file.read()
            print(contenido)
    except:
        print('No se pudo abrir el fichero porque no existe: ' + ruta)


def escribirArchivo1(ruta):
    print('------ Escritura archivo #1 -----')
    try:
        with open(ruta, 'w', encoding='utf-8') as file:
            file.write('esto es IPC2 Seccion D niños :v')
            print('Se escribio en el archivo correctamente')
    except:
        print('No se pudo abrir el fichero porque no existe: ' + ruta)
    print('----------------------------------')


def escribirArchivo2(ruta):
    print('------ Escritura archivo #2 -----')
    print('Escriba de nombre de Persona:')
    code = input()
    try:
        with open(ruta, 'a') as file:
            file.write(code)
            print('Se escribio en el archivo correctamente')
    except:
        print('No se pudo abrir el fichero porque no existe: ' + ruta)
    print('----------------------------------')


def escribirArchivo3(ruta):
    print('------ Escritura archivo #3 -----')
    code = '3era forma de escribir'
    try:
        with open(ruta, 'x') as file:
            file.write(code)
            print('Se escribio en el archivo correctamente')
    except:
        print('No se pudo abrir el fichero porque existe: ' + ruta)
    print('----------------------------------')


def Menu():
    opcion = 0
    while opcion != 7:
        print('----- Menu Ficheros -----')
        print('1. Leer Archivo Forma 1')
        print('2. Leer Archivo Forma 2')
        print('3. Leer Archivo Forma 3')
        print('4. Escribir Archivo Forma 1')
        print('5. Escribir Archivo Forma 2')
        print('6. Escribir Archivo Forma 3')
        print('7. Salir')
        opcion = input()
        ruta = ''
        if opcion == '1':
            print('Ingrese nombre fichero')
            ruta = input()
            leerArchivo1(ruta)
        elif opcion == '2':
            print('Ingrese nombre fichero')
            ruta = input()
            leerArchivo2(ruta)
        elif opcion == '3':
            print('Ingrese nombre fichero')
            ruta = input()
            leerArchivo3(ruta)
        elif opcion == '4':
            print('Ingrese nombre fichero')
            ruta = input()
            escribirArchivo1(ruta)
        elif opcion == '5':
            print('Ingrese nombre fichero')
            ruta = input()
            escribirArchivo2(ruta)
        elif opcion == '6':
            print('Ingrese nombre fichero')
            ruta = input()
            escribirArchivo3(ruta)
        else:
            opcion = 7

Menu()