from flask import Flask, request
from flask.json import jsonify
from manage import Manager
from xml.etree import ElementTree as ET

app = Flask(__name__)

manager = Manager()

@app.route('/')
def index():
    return "API Python with Flask Framework is working just fine!!!!"

@app.route('/add', methods=['POST'])
def add_character():
    xml = request.data.decode('utf-8')
    raiz = ET.XML(xml)
    for elemento in raiz:
        manager.add_character(elemento.attrib['name'], elemento.attrib['anime'], elemento.attrib['image'], elemento.text)
    return jsonify({'msg':'Archivo XML cargado correctamente :D'}), 200

@app.route('/showall', methods=['GET'])
def get_characters():
    c = manager.get_characters()
    return jsonify(c), 200


if __name__=='__main__':
    app.run(debug=True, port=4000)