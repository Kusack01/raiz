from django import forms
from django.forms import ModelForm
from .models import Producto,Usuario

class ProductoForm(ModelForm):
    class meta:
        model:Producto
        fields=['idProducto','nombre','precio','stock','idCategoria']

class UsuarioForm(ModelForm):
    class meta:
        model:Usuario