from django.shortcuts import render
from django.http import FileResponse
from app.forms import FileForm, AddForm, DeleteForm
from frontend.settings import PDF_FILES_FOLDER
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import requests
import io


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

def pdf_view(request): #frontend\app\common\coecys.pdf
    pdf = open(PDF_FILES_FOLDER + 'coecys.pdf', 'rb')
    return FileResponse(pdf)

def pdf_scratch(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)

    #Escribir linea por linea
    text_object = p.beginText(20, 20)
    #text_object.setTextOrigin()
    text_object.setFont('Helvetica', 14)
    estudiantes = [
        'Khristian',
        'Zetino',
        'Fernando',
        'Marjorie',
        'Yania',
        'Zenaida'
    ]

    for e in estudiantes:
        text_object.textLine(e)
    
    p.drawText(text_object)

    #poner imagenes
    #p.drawImage('C:/Users/javes/OneDrive/Desktop/LabIPC2/Clase 12/frontend/app/static/Usac_logo.png', 50, 50, width=150, height=150, mask='auto')

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    #p.drawString(20, 20, "HOLA LAB DE IPC2.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='lab.pdf')