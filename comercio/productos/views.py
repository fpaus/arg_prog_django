from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View
from .models import Categoria, Producto
from .forms import AgregarProd, FormContacto

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def categories(request):
    categorias = Categoria.objects.all()
    return render(request, 'productos/categories.html',{
        'categorias': categorias
    })
    
def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/productos.html',{
        'cosas' : productos,
        'nombre' : "Maximiliano"
    })

def agpro(request):
        print(request.POST)
        form = AgregarProd()
        return render(request, 'productos/agregarprod.html', {
            'form':form
        })
        
def contacto(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        print("POST")
        form = FormContacto(request.POST)
        if form.is_valid():
            # guardar en la base de datos 
            #mandar un mail
            print(form.cleaned_data)
            return render(request, 'contacto_enviado.html')
        else:
            print("formulario inválido")
            return render(request, 'error.html')
    else:
        print("GET")
        form = FormContacto()
    return render(request, 'contacto.html', {'form': form})