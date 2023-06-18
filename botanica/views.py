from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout
from .models import Usuario
from django.shortcuts import render, redirect

# Create your views here.
# Se puede crear una o ms vistas por cada html y al menos una url por vista.
#puede manipular request , urls y 
#http response,render,redirect.


def raiz2(request):
    return render(request,'botanica/Raiz-Botanica.html')

def recu (request):
    return render(request,'botanica/Recu.admin.html')

def recuperar (request):
    return render(request,'botanica/Recuperar.html')

def terminoycondicion (request):
    return render(request,'botanica/terycondi.html')

def venta (request):
    return render(request,'botanica/Venta.html')

def masetaterra (request):
    return render(request,'botanica/masetaTerra.html')

def maceterobio (request):
    return render(request,'botanica/maceteroBio.html')

def macetero1 (request):
    return render(request,'botanica/macetero1.html')
    
def macetabonsai (request):
    return render(request,'botanica/macetaBonsai.html')

def macetaexter (request):
    return render(request,'botanica/maceExter.html')

def ini (request):
    return render(request,'botanica/ini.html')

def crear_usu (request):
    return render(request,'botanica/Crear_usu.html')

def crear_admi (request):
    return render(request,'botanica/Crear_admi.html')

def contacto (request):
    return render(request,'botanica/Contacto.html')

def compralista (request):
    return render(request,'botanica/CompraLista.html')

def carrito (request):
    return render(request,'botanica/carrito.html')

def carrito_terracota (request):
    return render(request,'botanica/Carrito_terracota.html')

def carrito_bonsai (request):
    return render(request,'botanica/Carrito_bonsai.html')

def carrito_biodegradable (request):
    return render(request,'botanica/Carrito_biodegradable.html')

def agregar_editar_eliminar (request):
    return render(request,'botanica/agregar_editar_eliminar.html')

def acercade (request):
    return render(request,'botanica/acercade.html')

def metodo_pago (request):
    return render(request,'botanica/A_metodo_pago.html')

def editarcuenta(request):
    usuario = Usuario.objects.get(id=request.user.id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')

        usuario.nombre = nombre
        usuario.email = email
        usuario.save()

        return redirect('perfil')

    return render(request, 'botanica/editar_cuenta.html', {'usuario': usuario})

def codigo_recuperacion(request):
    return render(request,'botanica/codigo_recuperacion.html')