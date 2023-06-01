from django.db import models

# Create your models here.
class Region(models.Model):
    idRegion = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=15)


class Rol(models.Model):
    idRol = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=30)


class Pregunta(models.Model):
    idPregunta = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=200)


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)


class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    stock = models.IntegerField()
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


class Comuna(models.Model):
    idComuna = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=10)
    idRegion = models.ForeignKey(Region, on_delete=models.CASCADE)


class Direccion(models.Model):
    idDireccion = models.CharField(max_length=30, primary_key=True)
    calle = models.CharField(max_length=5)
    numero = models.IntegerField()
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)


class Usuario(models.Model):
    idUsuario = models.CharField(max_length=10, primary_key=True)
    rut = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=30)
    clave = models.CharField(max_length=15)
    idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    idPregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    idRespuesta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)


class Venta(models.Model):
    idVenta = models.CharField(max_length=15, primary_key=True)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fVenta = models.ImageField(upload_to="mascota")
    total = models.IntegerField()
    fDespacho = models.ImageField(upload_to="mascota")
    estatus = models.TextField(max_length=200)
    idDireccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    carrito = models.TextField(max_length=200)


class Detalle(models.Model):
    idDetalle = models.IntegerField(primary_key=True)
    idVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subTotal = models.IntegerField()


class Foto(models.Model):
    idFoto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15)

