from django import forms

class FileForm(forms.Form):
    file = forms.FileField(label="file")

class AddForm(forms.Form):
   name = forms.CharField(label="name")
   anime = forms.CharField(label="anime")
   desc = forms.CharField(label="desc")
   image = forms.CharField(label="image") 

class DeleteForm(forms.Form):
    name = forms.CharField(label="Nombre")