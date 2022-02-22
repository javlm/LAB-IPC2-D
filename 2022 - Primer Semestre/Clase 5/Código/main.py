from Lista_Simple import Lista_Simple
from xml.dom import minidom
import xml.etree.ElementTree as ET

lista_estudiantes = Lista_Simple()

def MiniDom(ruta):
    mydoc = minidom.parse(ruta)
    estudiante = mydoc.getElementsByTagName('estudiante') # pisps = mydoc.getElementsByTagName('piso')
    for e in estudiante: # for piso in pisos
        lista_estudiantes.insertFinal(e.attributes['nombre'].value, e.firstChild.data)
        #cursos = e.getElementsByTagName('curso') #patrones = piso.getElementsByTagName('patron')
        #for c in cursos:
        #    print('-',c.firstChild.data)


def elementTree(ruta):
    tree = ET.parse(ruta)
    raiz = tree.getroot()
    for r in raiz:
        carnet = r.text.replace('\n','')
        carnet = carnet.replace(' ', '')
        carnet = int(carnet)
        estudiante = lista_estudiantes.insertarEstudianteAlFinal(carnet, r.attrib['nombre'])
        #estudiante = lista_estudiantes.buscarEstudiante(carnet)
        print('Se inserto el estudiante con carnet:',estudiante.getCarnet())
        cursos = r[0]
        for c in cursos:
            estudiante.cursos.insertarCursoAlFinal(c.attrib['cod'], c.text)
        print('Se asignaron los siguientes cursos:')
        estudiante.cursos.mostrarCursos()

            

#MiniDom('./archivos/estudiantes.xml')  
elementTree('./archivos/estudiantes.xml')
#lista_estudiantes.showStudents()

