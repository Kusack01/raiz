from rest_framework import serializers
from botanica.models import Region, Rol, Pregunta, Categoria,Producto,Comuna,Direccion,Usuario,Venta,Detalle
class PruebaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields =['idRegion','nombre']
