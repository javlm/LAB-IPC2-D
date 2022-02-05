from lxml import etree as xp
from xml.etree import ElementTree as et

def xPath(ruta):
    tree = xp.parse(ruta)
    #Queries: //mamiferos//animal, //animal, //etiqueta[@atributo="valoratributo"]
    elementos = tree.xpath('//animal[@venenoso="si"]')

    print('Elementos de', ruta)
    for e in elementos: 
        print('Etiqueta', e.tag)
        print('Valor', e.text)
        print(e.attrib,'\n')

    print(len(elementos))


def elementTree(ruta):
    tree = et.parse(ruta)
    root = tree.getroot()
    print(root)

    print('Atributos')
    for element in root:
        for subelement in element:
            print(subelement.attrib)
        
    print('Valores')
    for element in root:
        for subelement in element:
            print(subelement.tag)
            print(subelement.text)

    print('Cantidad Mamiferos:',len(root[0])) #mamiferos = root[0] mamiferos =['tigre',...]
    print('Cantidad Serpientes:',len(root[1])) #serpientes = root[1] mamiferos =['tigre',...]
    print('Cantidad Lagartos:',len(root[2])) #lagartos = root[2] mamiferos =['tigre',...]
 
    
#xPath('zoo.xml')
elementTree('zoo.xml')