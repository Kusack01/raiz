#se puede quitar htmls y solo usar uno para todos los demas 
#solo que todos los demas no se pasan a django.
#,include
from django.contrib import admin
from django.urls import path
from .views import raiz2,venta,recu,recuperar,terminoycondicion,masetaterra,maceterobio
from .views import macetero1,macetabonsai,macetaexter,ini,crear_usu,crear_admi,contacto,compralista
from .views import carrito,carrito_terracota,carrito_bonsai,carrito_biodegradable,agregar_editar_eliminar
from .views import acercade,metodo_pago,editar_cuenta,codigo_recuperacion
from .import views 

urlpatterns = [
    path('',raiz2,name="raiz2"),
    path('Venta/',venta,name="venta"),
    path('Recu/',recu,name="recu"),
    path('Recuperar/',recuperar,name="recuperar"),
    path('Terminoycondicion/',terminoycondicion,name="terminoycondicion"),
    path('MacetaTerra/',masetaterra,name="masetaterra"),
    path('MaceteroBio/',maceterobio,name="maceterobio"),
    path('Macetero1/',macetero1,name="macetero1"),
    path('MacetaBonsai/',macetabonsai,name="macetabonsai"),
    path('MacetaExter/',macetaexter,name="macetaexter"),
    path('ini/',ini,name="ini"),
    path('CrearUsuario/',crear_usu,name="crear_usu"),
    path('CrearAdmin/',crear_admi,name="crear_admi"),
    path('Contacto/',contacto,name="contacto"),
    path('CompraLista/',compralista,name="compralista"),
    path('Carrito/',carrito,name="carrito"),
    path('CarritoTerracota/',carrito_terracota,name="carrito_terracota"),
    path('CarritoBonsai/',carrito_bonsai,name="carrito_bonsai"),
    path('CarritoBiodegradable/',carrito_biodegradable,name="carrito_biodegradable"),
    path('AgregarEditarEliminar/',agregar_editar_eliminar,name="agregar_editar_eliminar"),
    path('Acercade/',acercade,name="acercade"),
    path('MetododePago/',metodo_pago,name="metodo_pago"),
    path('cuentaeditar/',editar_cuenta, name='editar cuenta'),
    path('codigorecuperacion/',codigo_recuperacion,name="codigo_recuperacion")

]