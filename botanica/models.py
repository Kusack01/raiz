from django.db import models

# Create your models here.
class Comuna(models.Model):
    idComuna = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=10)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    
class Direccion(models.Model):
    idDireccion=models.CharField(max_length=30,primary_key=True)
    calle=models.CharField(max_length=5)
    numero=models.IntegerField(5)
    comuna=models.ForeignKey(Comuna,on_delete=models.CASCADE)
    idUsuario=models.ForeignKey(idDireccion, on_delete=models.CASCADE)
    

class Region(models.Model):
    idRegion=models.CharField(max_length=15,primary_key=True)
    nombre=models.CharField(max_length=15)
    

class Usuario(models.Model):
    idUsuario=models.CharField(max_length=10,primary_key=True)
    rut=models.IntegerField(12)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    telefono=models.IntegerField(11)
    correo=models.CharField(max_length=30)
    clave=models.CharField(max_length=15)
    idRol=models.ForeignKey(rut, on_delete=models.CASCADE)
    idPregunta=models.ForeignKey(rut, on_delete=models.CASCADE)
    idRespuesta=models.ForeignKey(rut, on_delete=models.CASCADE)
    

class Venta(models.Model):
    idVenta=models.CharField(max_length=15,primary_key=True)
    idUsuario=models.ForeignKey(idVenta, on_delete=models.CASCADE)
    fVenta=models.ImageField(upload_to="mascota")
    total=models.IntegerField(6)
    fDespacho=models.ImageField(upload_to="mascota")
    estatus=models.TextField(max_length=200)
    idDireccion=models.ForeignKey(idUsuario, on_delete=models.CASCADE)
    carrito=models.TextField(max_length=200)


class Rol(models.Model):
    idRol=models.CharField(max_length=15,primary_key=True)
    nombre=models.CharField(max_length=30)


class Pregunta(models.Model):
    idPregunta=models.IntegerField(15,primary_key=True)
    nombre=models.TextField(max_length=200)
 
    
class Detalle(models.Model):
    idDetalle=models.IntegerField(15,primary_key=True)
    idVenta=models.ForeignKey(idDetalle, on_delete=models.CASCADE)
    idProducto=models.ForeignKey(idVenta, on_delete=models.CASCADE)
    cantidad=models.IntegerField(3)
    subTotal=models.IntegerField(6)


class Producto(models.Model):
    idProducto=models.IntegerField(15,primary_key=True)
    nombre=models.CharField(max_length=30)
    precio=models.IntegerField(6)
    stock=models.IntegerField(3)
    idCategoria=models.ForeignKey(idProducto, on_delete=models.CASCADE)


class Categoria(models.Model):
    idCategoria=models.IntegerField(15,primary_key=True)
    nombre=models.CharField(max_length=15)


class Foto(models.Model):
    idFoto=models.IntegerField(15,primary_key=True)
    nombre=models.CharField(max_length=15)
    img=models.ImageField(upload_to="mascotas")
    idProducto=models.ForeignKey(idFoto, on_delete=models.CASCADE)