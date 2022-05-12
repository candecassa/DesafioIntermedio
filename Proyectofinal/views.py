from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template, loader

def saludo(request):
    return HttpResponse("Bienvenidos!!! En este sitio web veremos la información del Curso Python 2022")


def dia_de_hoy(request):
    dia=datetime.now()
    
    frase=f"hoy es: {dia}"
    return HttpResponse(frase)

def html(self):
    
    nom="CURSO PYTHON"
    num=[ 27620 ]
    diccionario={'nombre':nom, 'numero':num}
    
     
    plantilla=loader.get_template("inicio.html")
   
  
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)