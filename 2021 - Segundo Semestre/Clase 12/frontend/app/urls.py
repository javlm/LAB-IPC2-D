from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('cargar/', views.cargaMasiva, name='carga'),
    path('pdf/', views.pdf_view, name='pdf'),
    path('pdfs/', view=views.pdf_scratch, name='pdfs'),
]