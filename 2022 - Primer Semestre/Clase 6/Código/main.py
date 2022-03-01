
def leerArchivo():
    try:
        archivo = open('archivos/entrada.txt', encoding='utf-8')
        contenido = archivo.read()
        print(contenido)
    except:
        print('No se pudo abrir el archivo')
    finally:
        archivo.close()

def leerArchivo2():
    with open('archivos/entrada.txt', encoding='utf-8') as archivo:
        contenido = archivo.read()
    print(contenido)

def escribirArchivo(ruta, modo, contenido):
    try:
        with open(file=ruta, mode=modo, encoding='utf-8') as archivo:
            archivo.write(contenido)
    except Exception as e: 
        print('Error al manejar archivo', e)

escribirArchivo('archivos/modox.txt','x','Esto debe tirar error')
leerArchivo()
#escribirArchivo('archivos/entrada.txt', 'w', 'Esto sobrescribe el contenido')
#escribirArchivo('archivos/entrada.txt','a','Se inserto en la lista tal cosa 5\n')