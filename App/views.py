from ast import Return
from django.shortcuts import render
from .models import *
from App.forms import ProfeForm, EstudianteForm

# Create your views here.


def curso(request):
    return render(request, "App/curso.html")



def profesor(request):

    if request.method == 'POST':
       formulario= ProfeForm(request.POST)
       if formulario.is_valid():
           informacion=formulario.cleaned_data
           profesor=Profesor(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'])
       profesor.save()
       return render(request, "App/inicio.html")
    else: 
       formulario=ProfeForm()
       return render(request, "App/profesor.html",{'formulario':formulario})
       
    

def estudiante(request):
    if request.method == 'POST':
    
        formulario= EstudianteForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            estudiante=Estudiante(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'])
            estudiante.save()
            return render(request, "App/estudiante.html")

    else:
        formulario=EstudianteForm()
        return render(request, "App/estudiante.html",{'formulario':formulario})
       
       
    

def inicio(request):
    return render(request, "App/inicio.html")


def buscar(request):
    
    if request.GET['apellido']:
        apellido=request.GET['apellido']
        profesor=Profesor.objects.filter(apellido__icontains=apellido)
        return render(request, "App/resultados.html", {'profesor':profesor})
    else:
        respuesta="No se ingreso ningun apellido"
        return render(request, "App/inicio.html", {'respuesta':respuesta})
    

def entregable(request):
    return render(request, "App/entregable.html")
    
   

    


