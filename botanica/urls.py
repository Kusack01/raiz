#se puede quitar htmls y solo usar uno para todos los demas 
#solo que todos los demas no se pasan a django.
#,include
from django.contrib import admin
from django.urls import path ,include
from .views import index,raiz,venta,recu,recuperar,terminoycondicion,masetaterra,maceterobio
from .views import macetero1,macetabonsai,macetaexter,ini,crear_usu,crear_admi,contacto,compralista
from .views import carrito,carrito_terracota,carrito_bonsai,carrito_biodegradable,agregar_editar_eliminar
from .views import acercade,metodo_pago

urlpatterns = [
    path('index',index,name="index"),
    path('Raiz',raiz,name="raiz"),
    path('Venta',venta,name="venta"),
    path('Recu',recu,name="recu"),
    path('Recuperar',recuperar,name="recuperar"),
    path('Termino y condicion',terminoycondicion,name="terminoycondicion"),
    path('Maceta Terra',masetaterra,name="masetaterra"),
    path('Macetero Bio',maceterobio,name="maceterobio"),
    path('Macetero 1',macetero1,name="macetero1"),
    path('Maceta Bonsai',macetabonsai,name="macetabonsai"),
    path('Maceta Exter',macetaexter,name="macetaexter"),
    path('Ini',ini,name="ini"),
    path('Crear Usuario',crear_usu,name="crear_usu"),
    path('Crear Admin',crear_admi,name="crear_admi"),
    path('Contacto',contacto,name="contacto"),
    path('Compra Lista',compralista,name="compralista"),
    path('Carrito',carrito,name="carrito"),
    path('Carrito Terracota',carrito_terracota,name="carrito_terracota"),
    path('Carrito Bonsai',carrito_bonsai,name="carrito_bonsai"),
    path('Carrito Biodegradable',carrito_biodegradable,name="carrito_biodegradable"),
    path('Agregar Editar Eliminar',agregar_editar_eliminar,name="agregar_editar_eliminar"),
    path('Acerca de',acercade,name="acercade"),
    path('Metodo de Pago',metodo_pago,name="metodo_pago"),
]