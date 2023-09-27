from django import forms
from .models import Producto, Categoria

class FormContacto(forms.Form):
    nombre = forms.CharField(max_length=15)
    pregunta = forms.CharField(max_length=200)
    
class AgregarProd(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'observaciones', 'precio', 'stock']
    
class AgregarCat(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'tipo']
