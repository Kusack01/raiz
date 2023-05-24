from django.db import models

# Create your models here.

class direccion(models.Model):
    idDireccion=models.CharField(max_length=30,primary_key=True)
    calle=models.CharField(max_length=5)
    numero=models.IntegerField(5)
    idComuna=models.ForeignKey()
    idUsuario=models.ForeignKey()
    
class comuna(models.Model):
    idComuna=models.CharField(max_length=10,primary_key=True)
    nombre=models.CharField(max_length=10)
    idRegion=models.ForeignKey()
    
class region(models.Model):
    idRegion=models.CharField(max_length=15,primary_key=True)
    nombre=models.CharField(max_length=15)
    
class usuario(models.Model):
    idUsuario=models.CharField(max_length=10,primary_key=True)
    rut=models.IntegerField(12)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    telefono=models.IntegerField(11)
    correo=models.CharField(max_length=30)
    clave=models.CharField(max_length=15)
    idRol=models.ForeignKey()
    idPregunta=models.ForeignKey()
    idRespuesta=models.ForeignKey()
    
class venta(models.Model):
    idVenta=models.CharField(max_length=15,primary_key=True)
    idUsuario=models.ForeignKey()
    fVenta=models.ImageField(upload_to="mascota")
    total=models.IntegerField(6)
    fDespacho=models.ImageField(upload_to="mascota")
    estatus=models.TextField(max_length=200)
    idDireccion=models.ForeignKey()
    carrito=models.TextField(max_length=200)
    
class rol(models.Model):
    idRol=models.CharField(max_length=15,primary_key=True)
    nombre=models.CharField(max_length=30)
    
class pregunta(models.Model):
    idPregunta=models.IntegerField(15,primary_key=True)
    nombre=models.TextField(max_length=200)
    
class detalle(models.Model):
    idDetalle=models.IntegerField(15,primary_key=True)
    idVenta=models.ForeignKey()
    idProducto=models.ForeignKey()
    cantidad=models.IntegerField(3)
    subTotal=models.IntegerField(6)
    
class producto(models.Model):
    idProducto=models.IntegerField(15,primary_key=True)
    nombre=models.CharField(max_length=30)
    precio=models.IntegerField(6)
    stock=models.IntegerField(3)
    idCategoria=models.ForeignKey()
    
class categoria(models.Model):
    idCategoria=models.IntegerField(15,primary_key=True)
    nombre=models.CharField(max_length=15)
    
class foto(models.Model):
    idFoto=models.IntegerField(15,primary_key=True)
    nombre=models.CharField(max_length=15)
    img=models.ImageField(upload_to="mascotas")
    idProducto=models.ForeignKey()