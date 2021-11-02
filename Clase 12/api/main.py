from flask import Flask, request
from flask.json import jsonify
from manage import Manager
from xml.etree import ElementTree as ET

app = Flask(__name__)

manager = Manager()

@app.route('/')
def index():
    return "API Python with Flask Framework is working just fine!!!!"

@app.route('/add', methods = ['POST'])
def add():
    json = request.get_json()
    manager.add_character(json['name'], json['anime'], json['image'], json['desc'])
    return jsonify({'ok':True, 'msg':'Personaje agregado con exito'}), 200


@app.route('/addVarious', methods=['POST'])
def add_various():
    xml = request.data.decode('utf-8')
    raiz = ET.XML(xml)
    for elemento in raiz:
        manager.add_character(elemento.attrib['name'], elemento.attrib['anime'], elemento.attrib['image'], elemento.text)
    return jsonify({'ok':True, 'msg':'Archivo XML cargado correctamente :D'}), 200

@app.route('/showall', methods=['GET'])
def get_characters():
    c = manager.get_characters()
    return jsonify(c), 200

@app.route('/delete/<string:name', methods = ['DELETE'])
def delte_character(name):
    if request.method == 'DELETE':
        if name is not None:
            ok = manager.delete_character(name)
            if ok:
                return jsonify({'ok':ok, 'msg':'Personaje eliminado correctamente'}), 200
            else:
                return jsonify({'ok':ok, 'msg':'No existe el personaje'}), 404
        return jsonify({'ok': False, 'msg':'Solicitu incompleta'}), 500
    return jsonify({'msg':'Metodo no permitido'}), 405


if __name__=='__main__':
    app.run(debug=True, port=4000)