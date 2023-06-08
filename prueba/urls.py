from django.urls import path
from .views import lista_region

urlpatterns = [
    path('lista_region',lista_region,name="lista_region"),
    
    
]