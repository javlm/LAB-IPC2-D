from ListaSimple import ListaSimple
import xml.etree.ElementTree as ET

def cargarArchivo(ruta, estudiantes):
    tree = ET.parse(ruta)
    root = tree.getroot()
    for elemento in root:
        print('Estudiante',elemento.attrib['nombre'],'ha sido insertado.')
        estudiantes.crearEstudiante(elemento.attrib['carnet'], elemento.attrib['nombre']) # inserta estudiante
        for subelemento in elemento.iter('curso'):
            estudiante = estudiantes.getEstudiante(elemento.attrib['carnet'])#se busca estudiante
            estudiante.lista_cursos.insertar(subelemento.attrib['codigo'], subelemento.attrib['nombre'], subelemento.text) # se asigna curso
            print('Se asigno el curso', subelemento.attrib['nombre'],'al estudiante',estudiante.nombre)


def menu():
    opcion = ''
    Lista_Estudiantes = ListaSimple()
    while opcion != '8':
        print('------------ Menu --------------')
        print('1. Ingresar estudiante')
        print('2. Ver estudiantes inscritos')
        print('3. Eliminar estudiante')
        print('4. Asignar Curso')
        print('5. Ver cursos asignados de Estudiante')
        print('6. Cargar Archivo')
        print('7. Ordenamientos')
        opcion = input('Ingrese una opción: ')
        print(opcion)
        if opcion == '1':
            c = input('Ingrese numero de carnet: ')
            n = input('Ingrese nombre de estudiante: ')
            Lista_Estudiantes.crearEstudiante(c, n)
        elif opcion == '2':
            print('---------- Estudiantes Inscritos ----------', 'Total:',Lista_Estudiantes.size)
            Lista_Estudiantes.mostrarEstudiantes()
            print('-------------------------------------------')
        elif opcion == '4':
            carnet = input('Ingresar carnet de Estudiante: ')
            estudiante = Lista_Estudiantes.getEstudiante(carnet)
            if estudiante is None: 
                print('> Carnet incorrecto o no registrado')
            else: 
                code = input('Ingrese codigo de curso:')
                name = input('Ingrese nombre de curso:')
                cred = input('Ingrese cantidad de creditos de curso:')
                estudiante.lista_cursos.insertar(code, name, cred)
        elif opcion == '3':
            car = input('Ingrese carnet de estudiante a eliminar: ')            
            Lista_Estudiantes.eliminarEstudiante(car)
        elif opcion == '5':
            car = input('Ingrese carnet de estudiante: ')
            student = Lista_Estudiantes.getEstudiante(car)
            if student is None: 
                print('> Carnet incorrecto o no registrado')
            else:
                print('Estudiante:', student.nombre)
                print('-------Cursos-------')
                student.lista_cursos.mostrarCursos()
        elif opcion == '6':
            Filename = input('Ingrese nombre de archivo:')
            file = './' + Filename
            cargarArchivo(file, Lista_Estudiantes)
        elif opcion == '7':
            print('a. BubbleSort')
            print('b. InsertionSort')
            orden = input('Ingrese opcion:')
            if orden == 'a':
                Lista_Estudiantes.BubbleSort()
            if orden == 'b':
                Lista_Estudiantes.Insertion()
        else:
            break

menu()






