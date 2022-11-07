from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#Importo models
from appdesafio.models import *

# Create your views here.

#Se crea la funcion vista_familiares 

def vista_familiares(request):

    #Aqui obtengo los datos de la tabla Familia en la db
    listado_familiares = Familia.objects.all()

    #Creo el diccionario con la informacion
    datos = {"listado_familiares": listado_familiares}

    #Obtengo el template
    plantilla = loader.get_template("plantilla.html")

    #Renderizamos 
    documento = plantilla.render(datos)

    #Retornamos documento
    return HttpResponse(documento)