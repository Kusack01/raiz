from django.contrib import admin
from .models import direccion,comuna,region,usuario,venta,rol,pregunta,detalle
from .models import producto,categoria,foto

# Register your models here.

admin.site.register(direccion)
admin.site.register(comuna)
admin.site.register(region)
admin.site.register(usuario)
admin.site.register(venta)
admin.site.register(rol)
admin.site.register(pregunta)
admin.site.register(detalle)
admin.site.register(producto)
admin.site.register(categoria)
admin.site.register(foto)