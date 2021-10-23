from django.shortcuts import render
from app.forms import FileForm, AddForm, DeleteForm
import requests

# Create your views here.
endpoint = 'http://127.0.0.1:4000/'
def home(request):
    context = {
        'characters': []
    }
    try:
        respone = requests.get(endpoint + 'showall') # http://127.0.0.1:4000/showall
        characters = respone.json()
        context['characters'] = characters
    except:
        print('API no esta levantada')
    return render(request, 'index.html', context)

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            json_data = form.cleaned_data
            response = requests.post(endpoint + 'add', json=json_data)
            if response.ok:
                return render(request, 'add.html', {'form':form})
        return render(request, 'add.html', {'form':form})
    return render(request, 'add.html')

def delete(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            json_data = form.cleaned_data
            response = requests.delete(endpoint + 'delete/'+json_data['name'])
    else:
        form = DeleteForm()      
    return render(request, 'delete.html', {'form':form})  
    

def cargaMasiva(request):
    ctx = {
        'content':None,
        'response':None
    }
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            xml_binary = f.read()
            xml = xml_binary.decode('utf-8')
            ctx['content'] = xml
            response = requests.post(endpoint + 'addVarious', data=xml_binary)
            if response.ok:
                ctx['response'] = 'Archivo XML cargado corrrectamente'
            else:
                ctx['response'] = 'El archivo se envio, pero hubo un error en el servidor'
    else:
        return render(request, 'carga.html')
    return render(request, 'carga.html', ctx)