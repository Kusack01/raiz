from django.shortcuts import render

# Create your views here.
# Se puede crear una o ms vistas por cada html y al menos una url por vista.
#puede manipular request , urls y 
#http response,render,redirect.

def index (request):
    nombre=''
    return render(request,'menu/index.html')

def home(request):
    nombre='mauricio'

    contexto={
        'nom':nombre,
    }
    return render(request,'menu/home.html',contexto)

def borgona (request):
    nombreMascota="Borgoña"
    edadMascota=2
    razaMascota="Pitbull"
    lista=["marron","blanco","negro"]

    contexto={
        "nom":nombreMascota,
        "edad":edadMascota,
        "raza":razaMascota,
        "colores":lista
    }
    return render(request,'menu/borgona.html',contexto)
