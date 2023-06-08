from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from botanica.models import Region, Rol, Pregunta, Categoria,Producto,Comuna,Direccion,Usuario,Venta,Detalle
from prueba.serializers import PruebaSerializers
# Create your views here.
@csrf_exempt
@api_view(['GET','POST','DELETE'])
def lista_region(request):
    if request.method =='GET':
        region = Region.objects.all()
        serializer = PruebaSerializers(region,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer = PruebaSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
