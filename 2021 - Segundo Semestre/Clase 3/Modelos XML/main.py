from lxml import etree #xPath #modulo debe ser instalado win+r -> cmd -> pip install lxml
import xml.etree.ElementTree as ET #ElementTree
from xml.dom import minidom

def xPath(ruta):
    tree = etree.parse(ruta)
    elementos = tree.xpath('//mamiferos//animal')

    print('Todos los valores\n')
    for element in elementos:
        print('Etiqueta: ' + element.tag)
        print('Valor:' + element.text)
        print(element.attrib)
        print('\n')

def elT():
    tree = ET.parse('items.xml')
    raiz = tree.getroot()
    print(raiz)

    print('\nTodos los Atributos')
    for elemento in raiz: 
        for subelemento in elemento: 
            print(subelemento.attrib)

    for elemento in raiz:
        print(elemento.tag) #tag
        for subelemento in elemento:
            print('> ' + subelemento.text) #valores -> text

    print('\nUnico elmento:')
    print(raiz[1][0].text)

    print('cantidad')
    print(len(raiz[1]))

def MiniDom(ruta):
    mydoc = minidom.parse(ruta)
    items = mydoc.getElementsByTagName('game')

    #print('Valor de Atributos de elementos:')
    print(items[0].attributes['cat'].value)
    for el in items:
        print(el.attributes['cat'].value)

    print('\nSegundo Valor')
    print('forma 1: ' + items[0].childNodes[0].data)
    print('fomra 2: ' + items[0].firstChild.data)

    print('\nTodo los Valores:')
    for el in items:
        print(el.firstChild.data)

    print('\nCantidad:')
    print(len(items))   

elT()
MiniDom('items.xml')
xPath('animals.xml')