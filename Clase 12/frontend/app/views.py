from django.shortcuts import render
import requests
from requests.sessions import Request

# Create your views here.
endpoint = 'http://127.0.0.1:4000/'
def home(request):
    respone = requests.get(endpoint + 'showall') # http://127.0.0.1:4000/showall
    characters = respone.json()
    context = {
        'characters': characters
    }
    return render(request, 'index.html', context)