from Lista_Simple import Lista_Simple
from xml.dom import minidom
import xml.etree.ElementTree as ET

lista_estudiantes = Lista_Simple()

def MiniDom(ruta):
    mydoc = minidom.parse(ruta)
    estudiante = mydoc.getElementsByTagName('estudiante') # pisps = mydoc.getElementsByTagName('piso')
    for e in estudiante: # for piso in pisos
        lista_estudiantes.insertLast(e.attributes['nombre'].value, e.firstChild.data)
        #cursos = e.getElementsByTagName('curso') #patrones = piso.getElementsByTagName('patron')
        #for c in cursos:
        #    print('-',c.firstChild.data)


def elementTree(ruta):
    tree = ET.parse(ruta)
    raiz = tree.getroot()
    for r in raiz:
        nombre = r.text.replace('\n','')
        lista_estudiantes.insertLast(r.attrib['nombre'], nombre)
        #cursos = r[0]
        #for c in cursos:
        #    print('-',c.text)

#MiniDom('./archivos/estudiantes.xml')  
#elementTree('./archivos/estudiantes.xml')
lista_estudiantes.showStudents()

